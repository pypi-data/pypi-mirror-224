import json
from json import JSONDecodeError
from openssm.core.adapter.base_adapter import BaseAdapter
from openssm.core.slm.abstract_slm import AbstractSLM
from openssm.core.ssm.base_ssm import BaseSSM
from openssm.core.backend.rag_backend import AbstractRAGBackend
from openssm.core.slm.base_slm import PassthroughSLM
from openssm.core.prompts import Prompts
from openssm.utils.logs import Logs
from openssm.utils.utils import Utils


class RAGSSM(BaseSSM):
    rag_backend: AbstractRAGBackend = None

    def __init__(self,
                 slm: AbstractSLM = None,
                 rag_backend: AbstractRAGBackend = None,
                 name: str = None,
                 storage_dir: str = None):
        slm = slm or PassthroughSLM()
        self._rag_backend = rag_backend
        backends = [self.rag_backend] if self.rag_backend else None
        adapter = BaseAdapter(backends=backends)
        super().__init__(slm=slm, adapter=adapter, backends=backends, name=name, storage_dir=storage_dir)

    def is_passthrough(self) -> bool:
        return isinstance(self.slm, PassthroughSLM)

    @property
    def rag_backend(self) -> AbstractRAGBackend:
        return self._rag_backend

    def read_directory(self, storage_dir: str = None, use_existing_index: bool = False):
        self.storage_dir = storage_dir or self.storage_dir
        self.rag_backend.read_directory(self.storage_dir, use_existing_index)

    def read_gdrive(self, folder_id: str, storage_dir: str = None, use_existing_index: bool = False):
        self.storage_dir = storage_dir or self.storage_dir
        self.rag_backend.read_gdrive(folder_id, self.storage_dir, use_existing_index)

    def read_s3(self, s3_paths: str | set[str], storage_dir: str = None, use_existing_index: bool = False):
        self.storage_dir = storage_dir or self.storage_dir
        self.rag_backend.read_s3(s3_paths, self.storage_dir, use_existing_index)

    def read_website(self, urls: list[str], storage_dir: str = None, use_existing_index: bool = False):
        self.storage_dir = storage_dir or self.storage_dir
        self.rag_backend.read_website(urls, self.storage_dir, use_existing_index)

    @Logs.do_log_entry_and_exit()
    def _make_conversation(self, user_input: list[dict], rag_response: list[dict]) -> list[dict]:
        """
        Combines the user input and the RAG response into a single input.
        The user_input looks like this:
        [{"role": "user", "content": "What is the capital of Spain?"}]

        while the rag_response looks like this:
        [{"response": "Madrid is the capital of Spain."},]

        We want the combined conversation to look like this:
        [
            {"role": "system", "content": "<instructions>"},
            {"role": "user", "content": "<user question>"},
            {"role": "assistant1", "content": "<rag response>"}
        ]
        """
        system_instructions = Prompts.get_module_prompt(
            __name__, "_make_conversation", "system")

        if isinstance(user_input, list):
            user_input = user_input[0]
            if "content" in user_input:
                user_input = user_input["content"]
        user_input = str(user_input)

        if isinstance(rag_response, list):
            rag_response = rag_response[0]
            if "content" in rag_response:
                rag_response = rag_response["content"]
            elif "response" in rag_response:
                rag_response = rag_response["response"]
        rag_response = str(rag_response)

        combined_user_input = Prompts.get_module_prompt(
            __name__, "_make_conversation", "user"
            ).format(user_input=user_input, rag_response=rag_response)

        return [
            {"role": "system", "content": system_instructions},
            {"role": "user", "content": combined_user_input},
        ]

    # flake8: noqa: C901
    @Utils.do_canonicalize_user_input_and_query_response('user_input')
    @Logs.do_log_entry_and_exit()
    def discuss(self, user_input: list[dict], conversation_id: str = None) -> list[dict]:
        """
        An SSM with a RAG backend will reason between its own SLM’s knowledge
        and the knowledge of the RAG backend, before return the response.
        The process proceeds as follows:

        1. We first queries the RAG backend for a response.
        2. We then query the SLM, providing the initial query, as well as the
        response from the RAG backend as additional context.
        3. The SLM’s response is then returned.
        """
        # Get the RAG response.
        rag_response = None

        if self.rag_backend is not None:
            rag_response = self.rag_backend.query(user_input, conversation_id)
            # rag_response = self._sanitize_rag_response(rag_response)
            rag_response = rag_response[0]["response"]

        if isinstance(self.slm, PassthroughSLM):
            return rag_response

        # Get the SLM response.
        slm_response = self.slm.discuss(user_input, conversation_id)

        if rag_response is None:
            return slm_response

        # Combine the RAG response with the SLM response.
        user_input = user_input[0]["content"]
        slm_response = slm_response[0]["content"]

        combined_input = Prompts.get_module_prompt(
            __name__, "discuss", "combined_input").format(
                user_input=user_input,
                rag_response=rag_response,
                slm_response=slm_response)

        result = self.slm.discuss(combined_input, conversation_id)
        return result

    def _sanitize_rag_response(self, response) -> dict:
        # The response may be nested like so:
        # [{"role": "assistant", "content": "[{'role': 'assistant', 'details': 'xxx', 'content': 'What is the capital of Spain?'}]"}]
        # So we need to check for that and extract the content.
        if isinstance(response, list):
            temp = response[0]
            if "content" in temp:
                if isinstance(temp, dict):
                    temp = temp["content"]
                else:
                    temp = temp.content

                if isinstance(temp, list):
                    temp = temp[0]

                if isinstance(temp, dict):
                    # {"role": "assistant", "content": "What is the capital of Spain?"}
                    if "content" in temp:
                        response = temp
                elif isinstance(temp, str):
                    # "{\"role\": \"assistant\", \"content\": \"What is the capital of Spain?\"}}"
                    try:
                        response = json.loads(temp)
                    except JSONDecodeError as ex:  # pylint: disable=unused-variable
                        response = temp

        return response
