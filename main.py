from Intersection import Intersection

# 🔴🟡🟢🚶✋
def display_intersection(intersection, traffic_lights, pedestrian_lights):
    symbols = {
        "OFF":"⚫️",
        "RED":"🔴",
        "YELLOW":"🟡",
        "GREEN":"🟢",
        "WALK":"🚶",
        "STOP":"✋",
        "FLASHING_RED":"🛑"
    }
    key = {}
    for light_id, light in traffic_lights.items():
        key[str(light_id)] = symbols[light.state]
    for light_id, light in pedestrian_lights.items():
        key["P"+str(light_id)] = symbols[light.state]
    print(f"    P7 |   |   |   | 0 | 1 | 2 | P0    ")
    print(f"    {key["P7"]} |||||||||||||{key["0"]}  {key["1"]}  {key["2"]}  {key["P3"]}    ")
    print(f"P6{key["P6"]}                               {key["P1"]}P1")
    print(f"-                                   =--")
    print(f"11{key["11"]}                                =  ")
    print(f"-                                   =--")
    print(f"10{key["10"]}                                =  ")
    print(f"-                                   =--")
    print(f"9 {key["9"]}                                =  ")
    print(f"--=                                 =--")
    print(f"  =                                 {key["3"]}3")
    print(f"--=                                   -")
    print(f"  =                                 {key["4"]}4")
    print(f"--=                                   -")
    print(f"  =                                 {key["5"]}5")
    print(f"--=                                   -")
    print(f"P5{key["P5"]}                               {key["P2"]}P2")
    print(f"    {key["P4"]}   {key["8"]}  {key["7"]}  {key["6"]}||||||||||||| {key["P3"]}   ")
    print(f"    P4 | 8 | 7 | 6 |   |   |   | P3    ")

def simulate():
    intersection = Intersection()
    traffic_lights = {}
    pedestrian_lights = {}
    for signal_id, signal_group in intersection.signal_groups.items():
        for light in signal_group.lights:
            traffic_lights[light.light_id] = light
    for phase_id, phase_group in intersection.pedestrian_phase_groups.items():
        for light in phase_group.lights:
            pedestrian_lights[light.light_id] = light
    user_input = ""
    elapsed_time = 0
    while user_input != "QUIT":
        elapsed_time += 1
        intersection.tick()
        display_intersection(intersection, traffic_lights, pedestrian_lights)
        print(f"time elapsed: {elapsed_time} seconds")
        print(f"current phase timer: {intersection.traffic_controller.phase_timer} seconds")
        user_input = input("ID of pedestrian button that is hit(0-7):")
        if user_input in ["0", "1", "2", "3", "4", "5", "6", "7"]:
            intersection.button_pressed(int(user_input))
        user_input = input("Would you like to tick or quit(type \"QUIT\")?").upper()
    print("Simulation ended")


if __name__ == '__main__':
    simulate()
