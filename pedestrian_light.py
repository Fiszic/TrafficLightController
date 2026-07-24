
class PedestrianLight():
    def __init__(self, light_id):
        self.light_id = light_id
        self.state = "STOP" # STOP, WALK, OFF
        self.neutral_connected = True # Just for simulation purposes, but doesn't change anything otherwise

    def set_state(self, current_state):
        if not self.neutral_connected:
            self.state = "OFF"
            return
        self.state = current_state.upper()

    def __repr__(self):
        return f"[Ped Light {self.light_id}: {self.state}]"