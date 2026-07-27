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
    print(f"    P7 |   |   |   | 0 | 1 | 2 | P0    ")
    print(f"    ✋ |||||||||||||🔴  🔴  🔴  ✋    ")
    print(f"P6✋                               ✋P1")
    print(f"-                                   =--")
    print(f"11🔴                                =  ")
    print(f"-                                   =--")
    print(f"10🔴                                =  ")
    print(f"-                                   =--")
    print(f"9 🔴                                =  ")
    print(f"--=                                 =--")
    print(f"  =                                 🔴3")
    print(f"--=                                   -")
    print(f"  =                                 🔴4")
    print(f"--=                                   -")
    print(f"  =                                 🔴5")
    print(f"--=                                   -")
    print(f"P5✋                               ✋P2")
    print(f"    ✋  🔴  🔴  🔴|||||||||||||  ✋   ")
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
    display_intersection(intersection, traffic_lights, pedestrian_lights)





def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
