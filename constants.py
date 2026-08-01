class Ports:
    northbound_left = 5
    northbound_straight = 2
    eastbound_left = 7
    eastbound_straight = 4
    southbound_left = 1
    southbound_straight = 6
    westbound_left = 3
    westbound_straight = 8
    ped_NS_east = 9
    ped_EW_north = 10
    ped_NS_west = 11
    ped_EW_south = 12

class LightIDs:
    N_bound_left = [0]
    N_bound_straight = [1, 2]
    E_bound_left = [3]
    E_bound_straight = [4, 5]
    S_bound_left = [6]
    S_bound_straight = [7, 8]
    W_bound_left = [9]
    W_bound_straight = [10, 11]
    ped_NS_east = [1, 2]
    ped_EW_north = [0, 7]
    ped_NS_west = [5, 6]
    ped_EW_south = [3, 4]

class Durations:
    min_green_duration = 3
    green_duration = 6
    yellow_duration = 3
    red_duration = 1

class ButtonIDs:
    ped_NS_east = [1, 2]
    ped_EW_north = [0, 7]
    ped_NS_west = [5, 6]
    ped_EW_south = [3, 4]