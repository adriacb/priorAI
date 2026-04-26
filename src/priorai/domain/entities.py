from typing import Optional
from pydantic import BaseModel, Field

class LikelihoodEvidence(BaseModel):
    """Evidence parsed from news that affects the likelihood of risk."""
    likelihood_score: float = Field(..., description="Weight of the evidence, usually between 0 and 1.")
    confidence: float = Field(..., description="Confidence of the estimation.")
    justification: str = Field(..., description="Reasoning for the likelihood score.")

class BeliefState(BaseModel):
    """The current probabilistic belief state regarding a specific target."""
    target: str = Field(..., description="The target entity (e.g., company or sector).")
    probability: float = Field(..., description="The current probability of risk (Prior/Posterior).")
    context: str = Field(..., description="Historical context summary.")
