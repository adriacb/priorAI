from typing import Protocol
from priorai.domain.entities import BeliefState, LikelihoodEvidence

class ILikelihoodSensor(Protocol):
    """Contrato: Cualquier adaptador de LLM debe cumplir esto."""
    async def estimate(self, context: str, news: str) -> LikelihoodEvidence:
        ...

class IStateRepository(Protocol):
    """Contrato: Cualquier base de datos debe cumplir esto."""
    def save_state(self, company_id: str, state: BeliefState) -> None:
        ...
        
    def get_state(self, company_id: str) -> BeliefState:
        ...
