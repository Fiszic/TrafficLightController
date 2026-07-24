from traffic_light import TrafficLight
from pedestrian_light import PedestrianLight

class SignalGroup:
    def __init__(self, lights_ids, ports, ped_lights_ids=None):
        self.current_state = "RED"
        if ped_lights_ids is None:
            ped_lights_ids = []
        self.lights = []
        self.ped_lights = []
        self.ports = ports
        for light_id in lights_ids:
            self.lights.append(TrafficLight(light_id))
        for ped_light_id in ped_lights_ids:
            self.ped_lights.append(PedestrianLight(ped_light_id))
        self.pedestrian_light = False # Pedestrian light is walk or not
        self.queue_pedestrian = False # Pedestrian pressed the button to walk

    def get_ports(self):
        return self.ports

    def update_lights(self, color, phase_timer=0):
        if color == "GREEN" and self.queue_pedestrian and phase_timer == 1:
            self.queue_pedestrian = False
            self.pedestrian_light = True
        if color == "GREEN" and self.pedestrian_light:
            for ped_light in self.ped_lights:
                ped_light.set_state("WALK")
        if color == "YELLOW" and self.pedestrian_light:
            self.pedestrian_light = False
            for ped_light in self.ped_lights:
                ped_light.set_state("STOP")
        if color == "FLASHING_RED":
            self.pedestrian_light = False
            for ped_light in self.ped_lights:
                ped_light.set_state("STOP")
        for light in self.lights: # Simulates turning load switch on for the block
            light.set_state(color)
        self.current_state = color

    def queue_pedestrian(self, pedestrian):
        self.queue_pedestrian = True