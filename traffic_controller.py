from constants import Durations

class TrafficController:
    def __init__(self, intersection):
        self.phase_timer = 0
        self.current_phase = 0
        self.sequence = ["GREEN", "YELLOW", "RED"]
        self.current_sequence = 0
