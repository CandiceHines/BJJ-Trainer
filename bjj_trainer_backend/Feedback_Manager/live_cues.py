import random

class LiveCues:
    def __init__(self, user_name="Fighter", opponent_name="Opponent"):
        """Initialize cue categories with dynamic user and opponent names."""
        self.user_name = user_name
        self.opponent_name = opponent_name
        self.offensive_cues = {
            "grips": [
                "{user}, get him down!",
                "Go {user}, get him down now!",
                "{user}, get your grips!",
                "You need grips!"
            ],
            "de_la_riva": [
                "DLR, don’t stay here!",
                "{user}, you gotta move!",
                "DLR move his legs!"
            ],
            "guard": [
                "OK, Guard! Let's work!",
                "Sweep or triangle!",
                "{user}, get out of Guard!",
                "You gotta pass!"
            ],
            "side_control": [
                "Side Control, good!",
                "Progress or submit!"
            ],
            "mount": [
                "Mount nice!",
                "Choke or Armlock!"
            ],
            "back_control": [
                "Hooks in! Hooks in!",
                "Pump his face and armbar!"
            ],
            "applying_kimura": [
                "His watch! Your watch! Step over and paint the fence!"
            ],
            "applying_americana": [
                "His watch! Your watch! Paint the fence!"
            ],
            "applying_armbar": [
                "Pump his face and armbar!"
            ],
            "applying_bbb_choke": [
                "His gi behind the neck and baseball bat swing!"
            ],
            "applying_triangle": [
                "Pump his face and armbar!"
            ]
        }

        self.defensive_cues = {
            "defending_side_control": [
                "{user}, you gotta escape!",
                "Frame, Bridge, Knee-In!"
            ],
            "defending_mount": [
                "Stay calm, {user}!",
                "Push his knees down!"
            ],
            "defending_back_control": [
                "Protect the neck, {user}!",
                "Move a hook and slide!"
            ],
            "opponent_applying_kimura": [
                "Straight arm and use your knee to push away."
            ],
            "opponent_applying_americana": [
                "Grab your watch and head in!"
            ],
            "opponent_applying_armbar": [
                "Hitchhike! Hitchhike!"
            ],
            "opponent_applying_triangle": [
                "Stack him up and shoulder in!"
            ],
            "opponent_applying_bbb_choke": [
                "Roll into him!"
            ]
        }

    def get_offensive_cue(self, move_category):
        """Returns a formatted offensive cue based on category."""
        cue_list = self.offensive_cues.get(move_category, ["No offensive cue available for this category."])
        cue = random.choice(cue_list)
        return cue.format(user=self.user_name)

    def get_defensive_cue(self, move_category):
        """Returns a formatted defensive cue based on category."""
        cue_list = self.defensive_cues.get(move_category, ["No defensive cue available for this category."])
        cue = random.choice(cue_list)
        return cue.format(user=self.user_name)

# Example Usage:
if __name__ == "__main__":
    cues = LiveCues(user_name="Candice", opponent_name="David")
    
    # Simulating different match scenarios
    print("Offensive Cues:")
    print(cues.get_offensive_cue("grips"))
    print(cues.get_offensive_cue("guard"))

    print("\nDefensive Cues:")
    print(cues.get_defensive_cue("defending_mount"))
    print(cues.get_defensive_cue("opponent_applying_armbar"))

