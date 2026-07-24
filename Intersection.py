from constants import TerminalBlocks
from constants import LightIDs
from signal_group import SignalGroup
from traffic_controller import TrafficController

class Intersection:
    def __init__(self):
        self.status = "OP" # OP for operating and EF for emergency flashing
        self.traffic_controller = TrafficController(intersection=self)
        self.signal_groups = {
            0: SignalGroup(LightIDs.NS_bound_left,TerminalBlocks.southbound_left),
            1: SignalGroup(LightIDs.NS_bound_straight, TerminalBlocks.southbound_straight, LightIDs.ped_NS),
            2: SignalGroup(LightIDs.EW_bound_left, TerminalBlocks.westbound_left),
            3: SignalGroup(LightIDs.EW_bound_straight, TerminalBlocks.westbound_straight, LightIDs.ped_EW),
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