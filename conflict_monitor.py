
class ConflictMonitor:
    def __init__(self):
        return

    def safe_check(self, intersection):
        for phase_id, signal_group in intersection.signal_groups.items():
            light_states = [light.current_state for light in signal_group.lights]
            if "OFF" in light_states:
                print(f"[CMU FAULT]: Phase {phase_id} has an unpowered light.")
                return False
            if not all(state == signal_group.current_state for state in light_states):
                print(f"[CMU FAULT]: Phase {phase_id} has a stray light.")
                return False
        gy_count = 0 # Count Green and Yellows of signal groups
        for signal_group in intersection.signal_groups.values():
            if signal_group.current_state == "GREEN" or signal_group.current_state == "YELLOW":
                gy_count += 1
        if gy_count > 1:
            return False
        return True