# Determines offense vs. defense
class StateTracker:
    def __init__(self):
        """Track user and opponent states."""
        self.user_move = None
        self.opponent_move = None
        self.user_is_offensive = False
        self.last_update_time = None

    def update_state(self, user_move, opponent_move):
        """Update user & opponent moves and determine control."""
        self.user_move = user_move
        self.opponent_move = opponent_move

        # Determine if user is in control
        self.user_is_offensive = "Has" in user_move or "Applies" in user_move
        self.last_update_time = time.time()

    def get_user_status(self):
        """Returns if the user is on offense or defense."""
        return "Offense" if self.user_is_offensive else "Defense"

# Example Usage:
if __name__ == "__main__":
    tracker = StateTracker()
    
    tracker.update_state("Has Mount", "Defending Armbar")
    print(tracker.get_user_status())  # Output: Offense
    
    tracker.update_state("In Side Control", "Applies Kimura")
    print(tracker.get_user_status())  # Output: Defense
