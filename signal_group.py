from traffic_light import TrafficLight
from pedestrian_light import PedestrianLight

class SignalGroup:
    def __init__(self, lights_ids, ports, is_pedestrian_light):
        if is_pedestrian_light:
            self.current_state = "STOP"
            self.lights = []
            self.ports = ports
            for light_id in lights_ids:
                self.lights.append(PedestrianLight(light_id))
        else:
            self.current_state = "RED"
            self.lights = []
            self.ports = ports
            for light_id in lights_ids:
                self.lights.append(TrafficLight(light_id))

    def get_ports(self):
        return self.ports

    def update_lights(self, color, force_set=False):
        for light in self.lights: # Simulates turning load switch on for the block
            light.set_state(color, force_set)
        self.current_state = color