# File: core/scoring_engine.py

class ScoringEngine:
    def __init__(self):
        self.base_score = 100

    def compute_score(self, results):
        score = self.base_score
        for r in results:
            score += r.get("score_impact", 0)
        return max(0, min(score, 100))
