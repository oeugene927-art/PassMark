"""Decision Making Engine for Eugene AI"""

import random
from config.settings import DECISION_SETTINGS
from config.constants import STRATEGIES


class DecisionEngine:
    """Strategic decision-making system"""

    def __init__(self):
        """Initialize Decision Engine"""
        self.settings = DECISION_SETTINGS
        self.decisions_made = []
        self.strategy = "adaptive"
        self.confidence_scores = {}

    def evaluate_options(self, options, criteria=None):
        """Evaluate multiple options based on criteria"""
        scores = {}

        for option in options:
            score = self._calculate_option_score(option, criteria)
            scores[option] = score

        return sorted(scores.items(), key=lambda x: x[1], reverse=True)

    def _calculate_option_score(self, option, criteria):
        """Calculate score for an option"""
        if criteria is None:
            return random.random()

        score = 0
        for criterion, weight in criteria.items():
            value = option.get(criterion, 0) if isinstance(option, dict) else 0
            score += value * weight

        return score

    def make_decision(self, options, criteria=None, strategy=None):
        """Make a strategic decision"""
        strategy = strategy or self.strategy
        ranked_options = self.evaluate_options(options, criteria)

        if not ranked_options:
            return None

        if strategy == "aggressive":
            decision = ranked_options[0][0]
        elif strategy == "conservative":
            decision = ranked_options[-1][0]
        elif strategy == "balanced":
            mid_point = len(ranked_options) // 2
            decision = ranked_options[mid_point][0]
        elif strategy == "exploratory":
            decision = random.choice(options)
        else:  # adaptive or default
            if random.random() < self.settings["exploration_rate"]:
                decision = random.choice(options)
            else:
                decision = ranked_options[0][0]

        confidence = ranked_options[0][1] if ranked_options else 0
        self.decisions_made.append({
            'option': decision,
            'strategy': strategy,
            'confidence': confidence,
        })

        return decision

    def assess_risk(self, option, risk_factors=None):
        """Assess risk level for option"""
        if risk_factors is None:
            return 0.5

        total_risk = 0
        for factor, weight in risk_factors.items():
            factor_value = option.get(factor, 0) if isinstance(option, dict) else 0
            total_risk += factor_value * weight

        return min(1.0, total_risk)

    def optimize_strategy(self, outcomes):
        """Optimize decision strategy based on outcomes"""
        if not outcomes:
            return

        success_rate = sum(1 for outcome in outcomes if outcome.get('success', False)) / len(outcomes)

        if success_rate > 0.8:
            self.strategy = "aggressive"
        elif success_rate > 0.6:
            self.strategy = "balanced"
        else:
            self.strategy = "adaptive"

    def get_decision_history(self):
        """Get history of decisions made"""
        return self.decisions_made

    def __repr__(self):
        return f"DecisionEngine(Strategy: {self.strategy}, Decisions: {len(self.decisions_made)})"
