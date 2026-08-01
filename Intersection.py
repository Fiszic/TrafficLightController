from constants import Ports
from constants import ButtonIDs
from constants import LightIDs
from signal_group import SignalGroup
from traffic_controller import TrafficController
from traffic_light import TrafficLight
from pedestrian_light import PedestrianLight

class Intersection:
    def __init__(self):
        self.status = "OP" # OP for operating and EF for emergency flashing
        self.traffic_controller = TrafficController(intersection=self)
        self.traffic_lights = {
            "NBL": [],
            "NBS": [],
            "EBL": [],
            "EBS": [],
            "SBL": [],
            "SBS": [],
            "WBL": [],
            "WBS": []
        }
        self.pedestrian_lights = {
            "NS_east": [],
            "EW_south": [],
            "NS_west": [],
            "EW_north": [],
        }
        self.populate_lights()
        self.signal_groups = {
            1: SignalGroup(self.traffic_lights["NBL"] + self.traffic_lights["SBL"],
                           [Ports.southbound_left, Ports.northbound_left], False),
            2: SignalGroup(self.traffic_lights["NBS"] + self.traffic_lights["SBS"],
                           [Ports.southbound_straight, Ports.northbound_straight], False),
            3: SignalGroup(self.traffic_lights["EBL"] + self.traffic_lights["WBL"],
                           [Ports.westbound_left, Ports.eastbound_left], False),
            4: SignalGroup(self.traffic_lights["EBS"] + self.traffic_lights["WBS"],
                           [Ports.westbound_straight, Ports.eastbound_straight], False),
            #Emergency Groups
            5: SignalGroup(self.traffic_lights["NBL"] + self.traffic_lights["NBS"],
                           [Ports.northbound_left, Ports.northbound_straight], False),
            6: SignalGroup(self.traffic_lights["EBL"] + self.traffic_lights["EBS"],
                           [Ports.eastbound_left, Ports.eastbound_straight], False),
            7: SignalGroup(self.traffic_lights["SBL"] + self.traffic_lights["SBS"],
                           [Ports.southbound_left, Ports.southbound_straight], False),
            8: SignalGroup(self.traffic_lights["WBL"] + self.traffic_lights["WBS"],
                           [Ports.westbound_left, Ports.westbound_straight], False),
        }
        self.pedestrian_phase_groups = {
            2: SignalGroup(self.pedestrian_lights["NS_east"], [Ports.ped_NS_east], True),
            4: SignalGroup(self.pedestrian_lights["EW_south"], [Ports.ped_EW_south], True),
            6: SignalGroup(self.pedestrian_lights["NS_west"], [Ports.ped_NS_west], True),
            8: SignalGroup(self.pedestrian_lights["EW_north"], [Ports.ped_EW_north], True),
        }
        self.queued_ped_phases = set()
        self.go_ped_phases = set()
        self.inductive_phase_loops = {
            1: True,
            2: True,
            3: True,
            4: True
        }
        self.queued_emergency_phases = {}
        self.optical_sensors = {
            5: False, # Northbound sensors
            6: False, # Eastbound sensors
            7: False, # Southbound sensors
            8: False, # Westbound sensors
        }

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
        for optical_sensor, reading in self.optical_sensors.items():
            if reading:
                self.queued_emergency_phases[optical_sensor] = True
            elif self.queued_emergency_phases[optical_sensor]:
                self.queued_emergency_phases[optical_sensor] = False
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

    def populate_lights(self):
        for light_id in LightIDs.N_bound_left:
            self.traffic_lights["NBL"].append(TrafficLight(light_id))
        for light_id in LightIDs.N_bound_straight:
            self.traffic_lights["NBS"].append(TrafficLight(light_id))
        for light_id in LightIDs.E_bound_left:
            self.traffic_lights["EBL"].append(TrafficLight(light_id))
        for light_id in LightIDs.E_bound_straight:
            self.traffic_lights["EBS"].append(TrafficLight(light_id))
        for light_id in LightIDs.S_bound_left:
            self.traffic_lights["SBL"].append(TrafficLight(light_id))
        for light_id in LightIDs.S_bound_straight:
            self.traffic_lights["SBS"].append(TrafficLight(light_id))
        for light_id in LightIDs.W_bound_left:
            self.traffic_lights["WBL"].append(TrafficLight(light_id))
        for light_id in LightIDs.W_bound_straight:
            self.traffic_lights["WBS"].append(TrafficLight(light_id))

        for light_id in LightIDs.ped_NS_east:
            self.pedestrian_lights["NS_east"].append(PedestrianLight(light_id))
        for light_id in LightIDs.ped_EW_south:
            self.pedestrian_lights["EW_south"].append(PedestrianLight(light_id))
        for light_id in LightIDs.ped_NS_west:
            self.pedestrian_lights["NS_west"].append(PedestrianLight(light_id))
        for light_id in LightIDs.ped_EW_north:
            self.pedestrian_lights["EW_north"].append(PedestrianLight(light_id))