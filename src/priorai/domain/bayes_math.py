from priorai.domain.entities import BeliefState, LikelihoodEvidence

def apply_bayesian_update(prior: BeliefState, evidence: LikelihoodEvidence) -> BeliefState:
    """
    Applies Bayes' theorem to update the prior probability with new evidence.
    
    P(H|E) = P(E|H) * P(H) / P(E)
    
    Here we use a simplified version:
    Posterior Odds = Likelihood Ratio * Prior Odds
    
    If evidence is null (confidence = 0), the posterior should equal the prior.
    """
    if evidence.confidence == 0:
        return prior
        
    prior_prob = prior.probability
    
    # Avoid extreme values (0 or 1) for numerical stability
    prior_prob = max(1e-5, min(1 - 1e-5, prior_prob))
    
    # Convert prior to odds
    prior_odds = prior_prob / (1 - prior_prob)
    
    # Let likelihood ratio be evidence.likelihood_score
    # In a real scenario, this would be computed from a formal likelihood function.
    likelihood_ratio = evidence.likelihood_score
    
    # If likelihood_ratio is exactly 1.0 (neutral), odds remain the same
    # We factor in confidence: lower confidence pulls likelihood_ratio closer to 1.0
    effective_likelihood = 1.0 + (likelihood_ratio - 1.0) * evidence.confidence
    
    posterior_odds = effective_likelihood * prior_odds
    
    # Convert back to probability
    posterior_prob = posterior_odds / (1 + posterior_odds)
    
    # Create new state
    new_state = BeliefState(
        target=prior.target,
        probability=posterior_prob,
        context=prior.context
    )
    
    return new_state
