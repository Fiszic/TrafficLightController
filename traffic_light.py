class TrafficLight:
    def __init__(self, light_id):
        self.state = "RED" # RED, GREEN, YELLOW, OFF, FLASHING_RED
        self.light_id = light_id
        self.neutral_connected = True


    def set_state(self, current_state):
        if not self.neutral_connected:
            self.state = "OFF"
            return
        self.state = current_state

    def __repr__(self):
        return f"[Light {self.light_id}: {self.state}]"