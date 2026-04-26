from langgraph.graph import StateGraph, END
from priorai.infrastructure.state import AgenticState
from priorai.adapters.llm.relevance_agent import check_relevance
from priorai.adapters.llm.likelihood_agent import LikelihoodAgentSensor
from priorai.adapters.persistence.sql_repository import SQLRepository
from priorai.use_cases.update_belief_uc import process_new_evidence
from priorai.infrastructure.db_setup import SessionLocal

# Inicializamos los adaptadores
sensor = LikelihoodAgentSensor()
repo = SQLRepository()

async def filter_node(state: AgenticState):
    """Nodo que filtra si la noticia es relevante."""
    is_sig = await check_relevance(state['target'], state['news_content'])
    return {"is_significant": is_sig}

async def analyzer_updater_node(state: AgenticState):
    """Nodo que orquesta el análisis y la actualización (Usa el Caso de Uso)."""
    # Ejecutamos la lógica de negocio pura
    new_state = await process_new_evidence(
        company_id=state['company_id'],
        news=state['news_content'],
        prior_state=state['prior_state'],
        sensor=sensor,
        repo=repo
    )
    return {"posterior_state": new_state}

def should_continue(state: AgenticState):
    if state["is_significant"]:
        return "analyzer_updater"
    return END

# Configuración del Grafo
workflow = StateGraph(AgenticState)

workflow.add_node("filter", filter_node)
workflow.add_node("analyzer_updater", analyzer_updater_node)

workflow.set_entry_point("filter")

workflow.add_conditional_edges("filter", should_continue)
workflow.add_edge("analyzer_updater", END)

app = workflow.compile()
