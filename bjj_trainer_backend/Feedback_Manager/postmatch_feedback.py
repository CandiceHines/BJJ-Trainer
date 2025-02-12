import random

class FeedbackManager:
    def __init__(self):
        """Initialize feedback categories for post-match analysis."""
        self.feedback_templates = {
            "strong_takedown": [
                "Your takedown game was solid! Keep pressuring early to secure top control.",
                "Great job securing takedowns! Try setting them up with feints to increase success rate."
            ],
            "weak_takedown": [
                "Work on your takedowns—your opponent defended well. Try faking a shot to set up an entry.",
                "You struggled to get your opponent down. Focus on chaining takedown attempts together."
            ],
            "strong_guard_pass": [
                "Excellent guard passing! Your transitions were smooth and controlled.",
                "You passed the guard efficiently. Keep working on maintaining control after each pass."
            ],
            "weak_guard_pass": [
                "Your opponent retained guard well. Work on breaking grips and controlling the hips better.",
                "Try being more patient when passing the guard—set up your pass before exploding forward."
            ],
            "strong_control": [
                "You dominated positionally. Keep working on controlling your opponent before attacking.",
                "Great control time! Look to advance to more dominant positions quicker."
            ],
            "weak_control": [
                "You had trouble keeping top control. Work on your base and balance to maintain pressure.",
                "Your opponent escaped often. Try staying heavier on your hips and slowing down transitions."
            ],
            "strong_submissions": [
                "Your submissions were sharp! Keep refining your setups to finish even faster.",
                "Great job hunting for submissions! Keep focusing on wrist and grip control to force openings."
            ],
            "weak_submissions": [
                "You had multiple submission attempts, but they weren’t finished. Try tightening up your control before executing.",
                "Work on your submission setups—you had opportunities, but your opponent defended well."
            ],
            "strong_defense": [
                "Great defensive work! You escaped tough positions and stayed active under pressure.",
                "Your defense was impressive—keep working on reversing positions to get back on offense."
            ],
            "weak_defense": [
                "You spent too much time in defensive positions. Focus on escaping earlier in the exchange.",
                "Your opponent controlled you for long periods. Work on improving frames and hip movement."
            ]
        }

    def get_feedback(self, category):
        """Returns random feedback based on category."""
        return random.choice(self.feedback_templates.get(category, ["No feedback available for this category."]))

# Example Usage:
if __name__ == "__main__":
    feedback = FeedbackManager()
    print(feedback.get_feedback("strong_takedown"))
    print(feedback.get_feedback("weak_defense"))
