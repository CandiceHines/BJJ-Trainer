# Tracks and stores match statistics
import time
import json
import os

class MatchStats:
    def __init__(self, user_name="User", opponent_name="Opponent", save_path="match_logs.json"):
        self.user = user_name
        self.opponent = opponent_name
        self.start_time = time.time()
        self.user_control_time = 0
        self.opponent_control_time = 0
        self.opponent_reversals = 0
        self.last_control_switch = time.time()
        self.current_match_data = []

        self.save_path = save_path
        if not os.path.exists(self.save_path):
            with open(self.save_path, "w") as f:
                json.dump([], f)  # Initialize empty JSON file

    def update_control(self, user_is_offensive, move, confidence):
        """Tracks control time for both user and opponent & logs move data."""
        elapsed_time = time.time() - self.last_control_switch

        if user_is_offensive:
            self.user_control_time += elapsed_time
            control_status = "User in Control"
        else:
            self.opponent_control_time += elapsed_time
            self.opponent_reversals += 1
            control_status = "Opponent in Control"

        self.last_control_switch = time.time()

        # Store move in match data
        move_data = {
            "timestamp": round(time.time(), 2),
            "move": move,
            "confidence": round(confidence * 100, 2),
            "control_status": control_status
        }
        self.current_match_data.append(move_data)

    def end_match(self):
        """Saves match statistics to JSON and resets for next match."""
        total_time = round(time.time() - self.start_time, 2)
        
        match_data = {
            "fighter_name": self.user,
            "opponent_name": self.opponent,
            "match_time": total_time,
            "user_control_time": round(self.user_control_time, 2),
            "opponent_control_time": round(self.opponent_control_time, 2),
            "opponent_reversals": self.opponent_reversals,
            "match_moves": self.current_match_data
        }

        # Append to JSON file
        with open(self.save_path, "r+") as f:
            match_history = json.load(f)
            match_history.append(match_data)
            f.seek(0)
            json.dump(match_history, f, indent=4)

        print(f"📜 Match saved to {self.save_path}")

        return match_data

# Example Usage:
if __name__ == "__main__":
    stats = MatchStats(user_name="Candice", opponent_name="David")

    # Simulating match flow
    stats.update_control(True, "Has Mount", 0.85)
    time.sleep(3)

    stats.update_control(False, "In Side Control", 0.78)
    time.sleep(2)

    print(stats.end_match())  # Saves and outputs match summary


