from openssm.core.ssm.base_ssm import BaseSSM
from openssm.core.adapter.abstract_adapter import AbstractAdapter
from openssm.core.backend.abstract_backend import AbstractBackend
from openssm.integrations.lepton_ai.slm import SLM as LeptonSLM


class SSM(BaseSSM):
    def __init__(self,
                 adapter: AbstractAdapter = None,
                 backends: list[AbstractBackend] = None,
                 name: str = None):
        super().__init__(slm=LeptonSLM(), adapter=adapter, backends=backends, name=name)
