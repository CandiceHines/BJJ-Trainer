# Handles phase progression logic
import time
from live_cues import LiveCues

class PhaseManager:
    def __init__(self, user_name="Fighter", opponent_name="Opponent"):
        self.cues = LiveCues(user_name, opponent_name)
        self.user_name = user_name
        self.opponent_name = opponent_name
        self.last_cue_time = time.time()
        self.user_current_move = None
        self.opponent_current_move = None
        self.last_move_attempted = None
        self.user_stagnation_time = 0
        self.user_failed_attempts = 0

    def give_offensive_cue(self, move_category):
        """Provides an offensive cue when the user is attacking."""
        cue = self.cues.get_offensive_cue(move_category)
        print(f"{cue}")
        self.last_cue_time = time.time()
        self.last_move_attempted = move_category

    def give_defensive_cue(self, move_category):
        """Provides a defensive cue when the opponent is attacking."""
        cue = self.cues.get_defensive_cue(move_category)
        print(f"{cue}")
        self.last_cue_time = time.time()

    def update_user_move(self, current_move):
        """Tracks the user’s latest detected move."""
        self.user_current_move = current_move

    def update_opponent_move(self, current_move):
        """Tracks the opponent’s latest detected move."""
        self.opponent_current_move = current_move

    def check_progression(self):
        """Determines if the user successfully followed the training plan or failed due to opponent control."""
        current_time = time.time()
        time_elapsed = current_time - self.last_cue_time

        # Case 1: User successfully progressed
        if self.user_current_move != self.last_move_attempted and self.user_current_move is not None:
            print(f"{self.user_name} successfully transitioned to {self.user_current_move}.")
            self.user_failed_attempts = 0  # Reset failure counter
            return

        # Case 2: User is stuck and has not transitioned
        if self.user_current_move == self.last_move_attempted and time_elapsed > 5:
            print(f"{self.user_name}, you're stuck in {self.user_current_move}. You need to move!")
            self.give_offensive_cue(self.user_current_move)

        # Case 3: Opponent has taken control
        if "Has" in self.opponent_current_move or "Applying" in self.opponent_current_move:
            print(f"{self.opponent_name} has gained control! Switching to defensive cues.")
            self.user_failed_attempts += 1
            self.give_defensive_cue(self.opponent_current_move)

        # Case 4: User is stuck too long and failed to progress
        if time_elapsed > 8:
            print(f"{self.user_name}, you're still stuck! Reset and try again.")
            self.user_failed_attempts += 1

        # Case 5: If user has failed 3 times in a row, suggest an alternative approach
        if self.user_failed_attempts >= 3:
            print(f"{self.user_name}, the current strategy isn't working. Try a different transition.")

# Example Usage:
if __name__ == "__main__":
    phase_manager = PhaseManager(user_name="Candice", opponent_name="David")

    phase_manager.give_offensive_cue("grips")  # Initial offensive cue
    time.sleep(6)  # Simulating delay

    # Simulate the user failing to transition and opponent taking control
    phase_manager.update_user_move("Has Grips")  # User is still stuck
    phase_manager.update_opponent_move("Has Side Control")  # Opponent gains control
    phase_manager.check_progression()  # System will now adjust cues accordingly


