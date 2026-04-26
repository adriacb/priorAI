import pytest
from priorai.domain.entities import BeliefState, LikelihoodEvidence
from priorai.use_cases.update_belief_uc import process_new_evidence

class MockSensor:
    async def estimate(self, context: str, news: str) -> LikelihoodEvidence:
        return LikelihoodEvidence(
            likelihood_score=1.5,
            confidence=0.8,
            justification="Test justification"
        )

class MockRepository:
    def __init__(self):
        self.saved_state = None
        
    def save_state(self, company_id: str, state: BeliefState) -> None:
        self.saved_state = state
        
    def get_state(self, company_id: str) -> BeliefState:
        return BeliefState(target=company_id, probability=0.5, context="Test context")

@pytest.mark.asyncio
async def test_update_belief_use_case():
    sensor = MockSensor()
    repo = MockRepository()
    
    prior = BeliefState(target="company_1", probability=0.5, context="Test context")
    
    new_state = await process_new_evidence(
        company_id="company_1",
        news="Something bad happened.",
        prior_state=prior,
        sensor=sensor,
        repo=repo
    )
    
    assert new_state.probability > 0.5
    assert repo.saved_state == new_state
