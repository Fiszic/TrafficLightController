class TrafficLight:
    def __init__(self, light_id):
        self.state = "RED" # RED, GREEN, YELLOW, OFF, FLASHING_RED
        self.light_id = light_id
        self.neutral_connected = True
        self.rogue_state = False

    def set_state(self, current_state, force_set):
        if not self.neutral_connected:
            self.state = "OFF"
            return
        if not self.rogue_state or force_set:
            self.state = current_state

    def __repr__(self):
        return f"[Light {self.light_id}: {self.state}]"