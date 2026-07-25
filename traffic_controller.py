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
            self.current_signal_group = self.current_signal_group % 4
            self.current_sequence = 0
            self.phase_timer = 0
        self.send_control_signals()

    def send_control_signals(self):
        current_color = self.sequence[self.current_sequence]
        gy_count = 0 # Count the number of Green and Yellow lights in each signal group(Should not exceed 1)
        for group_id, signal_group in self.intersection.signal_groups.items():
            if group_id == self.current_signal_group + 1:
                if current_color in ["GREEN", "YELLOW"]:
                    gy_count += 1
                    signal_group.update_lights(current_color)
                else:
                    signal_group.update_lights("RED")
            else:
                signal_group.update_lights("RED")

        for phase_id, phase_group in self.intersection.pedestrian_phase_groups.items():
            if phase_id in self.intersection.go_ped_phases and current_color == "YELLOW":
                phase_group.update_lights("STOP")
                self.intersection.go_ped_phases.remove(phase_id)
            elif phase_id in self.intersection.go_ped_phases and current_color == "GREEN":
                phase_group.update_lights("WALK")
            elif phase_id in self.intersection.queued_ped_phases and current_color == "GREEN" and self.phase_timer == 1:
                if self.current_signal_group + 1 == 2 and phase_id in [2, 6]:
                    phase_group.update_lights("WALK")
                    self.intersection.go_ped_phases.add(phase_id)
                    self.intersection.queued_ped_phases.remove(phase_id)
                elif self.current_signal_group + 1 == 4 and phase_id in [4, 8]:
                    phase_group.update_lights("WALK")
                    self.intersection.go_ped_phases.add(phase_id)
                    self.intersection.queued_ped_phases.remove(phase_id)
                else:
                    phase_group.update_lights("STOP")
            else:
                phase_group.update_lights("STOP")
        if not self.conflict_monitor.safety_check(self.intersection, gy_count, self.current_signal_group): # Does safety checks from CMU
            self.intersection.set_emergency_status()