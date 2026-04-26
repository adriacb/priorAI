from priorai.domain.entities import BeliefState
from priorai.domain.bayes_math import apply_bayesian_update
from priorai.domain.ports import ILikelihoodSensor, IStateRepository

async def process_new_evidence(
    company_id: str,
    news: str,
    prior_state: BeliefState,
    sensor: ILikelihoodSensor,     # Inyección de dependencia
    repo: IStateRepository         # Inyección de dependencia
) -> BeliefState:
    
    # 1. Obtenemos la evidencia a través del puerto (PydanticAI por debajo)
    evidence = await sensor.estimate(prior_state.context, news)
    
    # 2. Matemática pura
    new_state = apply_bayesian_update(prior_state, evidence)
    
    # 3. Guardamos a través del puerto (SQLAlchemy por debajo)
    repo.save_state(company_id, new_state)
    
    return new_state
