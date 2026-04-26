import pytest
from priorai.domain.entities import BeliefState, LikelihoodEvidence
from priorai.domain.bayes_math import apply_bayesian_update

def test_bayes_math_neutral_evidence():
    """Prueba unitaria de la fórmula (Obligatorio)"""
    prior = BeliefState(target="Test", probability=0.5, context="")
    
    # Evidencia nula o neutral (confidence = 0)
    evidence = LikelihoodEvidence(likelihood_score=2.0, confidence=0.0, justification="")
    
    posterior = apply_bayesian_update(prior, evidence)
    
    # Si la evidencia es nula, el posterior sigue siendo 0.5
    assert posterior.probability == 0.5

def test_bayes_math_strong_evidence():
    prior = BeliefState(target="Test", probability=0.5, context="")
    
    # Fuerte evidencia de riesgo
    evidence = LikelihoodEvidence(likelihood_score=3.0, confidence=1.0, justification="")
    
    posterior = apply_bayesian_update(prior, evidence)
    
    assert posterior.probability > 0.5
