from constants import Ports
from constants import ButtonIDs
from constants import LightIDs
from signal_group import SignalGroup
from traffic_controller import TrafficController

class Intersection:
    def __init__(self):
        self.status = "OP" # OP for operating and EF for emergency flashing
        self.traffic_controller = TrafficController(intersection=self)
        self.signal_groups = {
            1: SignalGroup(LightIDs.NS_bound_left,[Ports.southbound_left, Ports.northbound_left], False),
            2: SignalGroup(LightIDs.NS_bound_straight, [Ports.southbound_straight, Ports.northbound_straight], False),
            3: SignalGroup(LightIDs.EW_bound_left, [Ports.westbound_left, Ports.eastbound_left], False),
            4: SignalGroup(LightIDs.EW_bound_straight, [Ports.westbound_straight, Ports.eastbound_straight], False),
        }
        self.pedestrian_phase_groups = {
            2: SignalGroup(LightIDs.ped_NS_east, [Ports.ped_NS_east], True),
            4: SignalGroup(LightIDs.ped_EW_south, [Ports.ped_EW_south], True),
            6: SignalGroup(LightIDs.ped_NS_west, [Ports.ped_NS_west], True),
            8: SignalGroup(LightIDs.ped_EW_north, [Ports.ped_EW_north], True),
        }
        self.queued_ped_phases = set()
        self.go_ped_phases = set()

    def set_emergency_status(self):
        self.status = "EF"
        print("Emergency Flash Engaged")

    def tick(self):
        if self.status == "EF":
            for signal_group in self.signal_groups.values():
                signal_group.update_lights("FLASHING_RED", True)
            for signal_group in self.pedestrian_phase_groups.values():
                signal_group.update_lights("STOP", True)
            return
        self.traffic_controller.tick()

    def button_pressed(self, button):
        if button in ButtonIDs.ped_NS_east:
            self.queued_ped_phases.add(2)
        elif button in ButtonIDs.ped_EW_south:
            self.queued_ped_phases.add(4)
        elif button in ButtonIDs.ped_NS_west:
            self.queued_ped_phases.add(6)
        elif button in ButtonIDs.ped_EW_north:
            self.queued_ped_phases.add(8)