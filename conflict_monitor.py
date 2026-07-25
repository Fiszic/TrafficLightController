
class ConflictMonitor:
    def __init__(self):
        return

    def safety_check(self, intersection, gy_count, current_signal_group):
        if gy_count > 1:
            print(f"[CMU FAULT]: Multiple go light phases.")
            return False
        for signal_id, signal_group in intersection.signal_groups.items():
            light_states = [light.current_state for light in signal_group.lights]
            if "OFF" in light_states:
                print(f"[CMU FAULT]: Signal group {signal_id} has an unpowered light.")
                return False
            if not all(state == signal_group.current_state for state in light_states):
                print(f"[CMU FAULT]: Signal group {signal_id} has a stray light.")
                return False
        for phase_id, phase_group in intersection.pedestrian_phase_groups.items():
            if phase_group.current_state == "WALK":
                if current_signal_group in [0, 2]:
                    print(f"[CMU FAULT]: Pedestrian Phase {phase_id} has a walk signal at the wrong time.")
                    return False
                if current_signal_group + 1 == 2 and phase_id in [4, 8]:
                    print(f"[CMU FAULT]: Pedestrian Phase {phase_id} has a walk signal at the wrong time.")
                    return False
                if current_signal_group + 1 == 4 and phase_id in [2, 6]:
                    print(f"[CMU FAULT]: Pedestrian Phase {phase_id} has a walk signal at the wrong time.")
                    return False
            light_states = [light.current_state for light in phase_group.lights]
            if phase_group.current_state != "WALK" and any(state == "WALK" for state in light_states):
                print(f"[CMU FAULT]: Pedestrian Phase {phase_id} has a stray light.")
                return False
        return True