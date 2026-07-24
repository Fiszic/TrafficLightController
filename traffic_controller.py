from conflict_monitor import ConflictMonitor
from constants import Durations

class TrafficController:
    def __init__(self, intersection):
        self.phase_timer = 0
        self.current_signal_group = 0
        self.sequence = ["GREEN", "YELLOW", "RED"]
        self.current_sequence = 0
        self.conflict_monitor = ConflictMonitor()
        self.intersection = intersection

    def tick(self):
        self.phase_timer += 1
        current_color = self.sequence[self.current_sequence]
        if current_color == "GREEN" and self.phase_timer >= Durations.green_duration:
            self.current_sequence += 1
            self.phase_timer = 0
        elif current_color == "YELLOW" and self.phase_timer >= Durations.yellow_duration:
            self.current_sequence += 1
            self.phase_timer = 0
        elif current_color == "RED" and self.phase_timer >= Durations.red_duration:
            self.current_signal_group = (self.current_signal_group + 1) % 4
            self.current_sequence = 0
            self.phase_timer = 0
        self.send_control_signals()

    def send_control_signals(self):
        current_color = self.sequence[self.current_sequence]
        gy_count = 0 # Count the number of Green and Yellow lights in each signal group(Should not exceed 1)
        for group_id, signal_group in self.intersection.signal_groups.items():
            if group_id == self.current_signal_group:
                if current_color in ["GREEN", "YELLOW"]:
                    gy_count += 1
                    signal_group.update_lights(current_color)
                else:
                    signal_group.update_lights("RED")
            else:
                signal_group.update_lights("RED")
        if not self.conflict_monitor.safety_check(self.intersection, gy_count): # Does safety checks from CMU
            self.intersection.set_emergency_status()