from traffic_light import TrafficLight
from pedestrian_light import PedestrianLight

class SignalGroup:
    def __init__(self, lights, ports, is_pedestrian_light):
        self.lights = lights
        self.ports = ports
        if is_pedestrian_light:
            self.current_state = "STOP"
        else:
            self.current_state = "RED"

    def get_ports(self):
        return self.ports

    def update_lights(self, color, force_set=False):
        for light in self.lights: # Simulates turning load switch on for the block
            light.set_state(color, force_set)
        self.current_state = color