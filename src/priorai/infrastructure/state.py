from typing import TypedDict
from priorai.domain.entities import BeliefState, LikelihoodEvidence

class AgenticState(TypedDict):
    """El estado que viaja por el grafo de LangGraph."""
    company_id: str
    target: str                  # Ej: "CaixaBank" o "Sector Inmobiliario"
    news_content: str
    is_significant: bool         # Resultado del filtro
    prior_state: BeliefState     # Lo que recuperamos de SQL
    evidence: LikelihoodEvidence # Lo que el LLM infiere
    posterior_state: BeliefState # El resultado final
