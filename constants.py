class TerminalBlocks:
    northbound_left = 5
    northbound_straight = 2
    eastbound_left = 7
    eastbound_straight = 4
    southbound_left = 1
    southbound_straight = 6
    westbound_left = 3
    westbound_straight = 8


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