from priorai.domain.ports import ILikelihoodSensor
from priorai.domain.entities import LikelihoodEvidence
from pydantic_ai import Agent

# Define the Agent
likelihood_agent = Agent(
    'openai:gpt-4o',
    result_type=LikelihoodEvidence,
    system_prompt="""Evalúa la noticia dada respecto al contexto de la empresa.
    Determina cómo afecta a la probabilidad de riesgo.
    Devuelve un LikelihoodEvidence con un likelihood_score (ratio, 1.0 es neutral),
    una confidence (0.0 a 1.0) y una justification.
    """
)

class LikelihoodAgentSensor(ILikelihoodSensor):
    """Implementa el puerto ILikelihoodSensor usando PydanticAI."""
    
    async def estimate(self, context: str, news: str) -> LikelihoodEvidence:
        prompt = f"Context: {context}\n\nNews: {news}"
        result = await likelihood_agent.run(prompt)
        return result.data
