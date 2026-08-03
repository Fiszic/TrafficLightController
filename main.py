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
    print(f"    {key["P7"]} |||||||||||||{key["0"]}  {key["1"]}  {key["2"]}  {key["P0"]}    ")
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
    for inductive_sensor, reading in intersection.inductive_phase_loops.items():
        print(f"Inductive sensors for phase {inductive_sensor} : {reading}")
    emergency_phase_key = {
        5: "North-bound",
        6: "East-bound",
        7: "South-bound",
        8: "West-bound",
    }
    for optical_sensor, reading in intersection.optical_sensors.items():
        print(f"Optical sensors for phase {emergency_phase_key[optical_sensor]} traffic : {reading}")

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
        user_input = input("Add detection(\"DET\") or remove detection(\"REM\") of car. Press ENTER to skip.")
        if user_input == "DET":
            phase = input("Enter the phase number of detection added.")
            intersection.inductive_phase_loops[int(phase)] = True
        elif user_input == "REM":
            phase = input("Enter the phase number of detection removed.")
            intersection.inductive_phase_loops[int(phase)] = False
        user_input = input("ID of pedestrian button that is pressed(0-7). Press ENTER to skip:")
        if user_input in ["0", "1", "2", "3", "4", "5", "6", "7"]:
            intersection.button_pressed(int(user_input))
        user_input = input("Add detection(\"DET\") or remove detection(\"REM\") of emergency vehicle. Press ENTER to skip.")
        if user_input == "DET":
            sensor = input("ID of optical sensor detecting emergency vehicle(5-8).")
            intersection.optical_sensors[int(sensor)] = True
        if user_input == "REM":
            sensor = input("ID of optical sensor detecting emergency vehicle(5-8).")
            intersection.optical_sensors[int(sensor)] = False
        user_input = input("Type \"TL\" or \"PED\" to cause a malfunction. Press ENTER to skip.")
        if user_input == "TL":
            id_input = input("ID of the traffic light malfunction.")
            state_input = (input("State of the traffic light malfunction.")).upper()
            if state_input == "OFF":
                traffic_lights[int(id_input)].neutral_connected = False
            else:
                traffic_lights[int(id_input)].state = state_input
                traffic_lights[int(id_input)].rogue_state = True
        if user_input == "PED":
            id_input = input("ID of the pedestrian light malfunction.")
            state_input = (input("State of the pedestrian light malfunction.")).upper()
            if state_input == "OFF":
                pedestrian_lights[int(id_input)].neutral_connected = False
            else:
                pedestrian_lights[int(id_input)].state = state_input
                traffic_lights[int(id_input)].rogue_state = True
        user_input = input("Would you like to quit(type \"QUIT\")? Press ENTER to continue to next tick.").upper()
    print("Simulation ended.")


if __name__ == '__main__':
    simulate()
