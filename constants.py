class TerminalBlocks:
    southbound_left = "Block_A"
    southbound_straight = "Block_B"
    westbound_left = "Block_C"
    westbound_straight = "Block_D"
    northbound_left = "Block_E"
    northbound_straight = "Block_F"
    eastbound_left = "Block_G"
    eastbound_straight = "Block_H"

class LightIDs:
    NS_bound_left = [0, 6]
    NS_bound_straight = [1, 2, 7, 8]
    EW_bound_left = [3, 9]
    EW_bound_straight = [4, 5, 10, 11]
    ped_NS = [1, 2, 5, 6]
    ped_EW = [0, 3, 4, 7]

class Durations:
    green_duration = 6
    yellow_duration = 3
    red_duration = 1