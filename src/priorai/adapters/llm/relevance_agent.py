from pydantic_ai import Agent

relevance_agent = Agent(
    'openai:gpt-4o',
    result_type=bool,
    system_prompt="""Decide si esta noticia es SIGNIFICATIVA para el riesgo de {target}. 
    Solo di True si reporta cambios estructurales, financieros o legales graves. 
    Di False si es opinión, ruido de mercado o eventos menores."""
)

async def check_relevance(target: str, news_content: str) -> bool:
    """Invokes the relevance agent."""
    is_sig = await relevance_agent.run(news_content, deps=target)
    return is_sig.data
