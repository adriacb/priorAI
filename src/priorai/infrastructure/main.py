import asyncio
from priorai.infrastructure.graph_workflow import app
from priorai.adapters.persistence.sql_repository import SQLRepository

async def main():
    repo = SQLRepository()
    
    # Dummy company for test
    company_id = "test_corp_01"
    target_name = "Test Corporation"
    
    # Obtener el prior
    prior = repo.get_state(company_id)
    prior.target = target_name
    
    news = "Test Corp acaba de anunciar una fusión con su mayor competidor, duplicando su cuota de mercado."
    
    initial_state = {
        "company_id": company_id,
        "target": target_name,
        "news_content": news,
        "prior_state": prior
    }
    
    print(f"--- Procesando Noticia para {target_name} ---")
    print(f"News: {news}")
    print(f"Prior Probability: {prior.probability}")
    
    # Ejecutar el grafo
    result = await app.ainvoke(initial_state)
    
    if result.get("is_significant"):
        print("La noticia FUE considerada significativa.")
        print(f"Posterior Probability: {result['posterior_state'].probability}")
    else:
        print("La noticia NO fue significativa. Se ignoró.")

if __name__ == "__main__":
    asyncio.run(main())
