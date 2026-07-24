
class ConflictMonitor:
    def __init__(self):
        return

    def safety_check(self, intersection, gy_count):
        if gy_count > 1:
            return False
        for phase_id, signal_group in intersection.signal_groups.items():
            light_states = [light.current_state for light in signal_group.lights]
            if "OFF" in light_states:
                print(f"[CMU FAULT]: Phase {phase_id} has an unpowered light.")
                return False
            if not all(state == signal_group.current_state for state in light_states):
                print(f"[CMU FAULT]: Phase {phase_id} has a stray light.")
                return False
            if (not signal_group.current_state == "GREEN") and signal_group.pedestrian_light:
                print(f"[CMU FAULT]: Phase {phase_id} has a stray pedestrian walk light.")
                return False
        return True