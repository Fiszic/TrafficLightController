from constants import Ports
from constants import LightIDs
from signal_group import SignalGroup
from traffic_controller import TrafficController

class Intersection:
    def __init__(self):
        self.status = "OP" # OP for operating and EF for emergency flashing
        self.traffic_controller = TrafficController(intersection=self)
        self.signal_groups = {
            1: SignalGroup(LightIDs.NS_bound_left,Ports.southbound_left),
            2: SignalGroup(LightIDs.NS_bound_straight, Ports.southbound_straight, LightIDs.ped_NS),
            3: SignalGroup(LightIDs.EW_bound_left, Ports.westbound_left),
            4: SignalGroup(LightIDs.EW_bound_straight, Ports.westbound_straight, LightIDs.ped_EW),
        }

    def set_emergency_status(self):
        self.status = "EF"
        print("Emergency Flash Engaged")

    def tick(self):
        if self.status == "EF":
            for signal_group in self.signal_groups.values():
                for light in signal_group.lights:
                    light.set_state("FLASHING_RED")
            return
        self.traffic_controller.tick()