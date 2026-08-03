# Traffic Light Controller Simulator
This is a python-based simulator that models a traffic light controller. 
To model real-world intersection behavior, the simulation uses finite state machines, configurable timing, and mimics real-world sensors, creating event-driven inputs.

## Features
- Full 4-way intersection
- ASCII intersection visualization
- Traffic phases
- Signal groups
- Pedestrian crossing
- Pedestrian push buttons
- Vehicle detection using inductive loops
- Conflict monitoring for traffic and pedestrian lights
- Emergency vehicle pre-emption using optical sensors
- Configurable timing parameters

## Demo

## Architecture

In this simulation, the intersection object is the main container class of the traffic controller. It holds all variables, objects, and functions that base the functioning of the traffic light controller. This includes all objects for the lights, phases, and sensor readings. Furthermore, it includes the main functionality in case the controller is in a fail state, allowing for direct and immediate control. The traffic light controller class is the main center of operations, handling light rotations, deciding when to activate pedestrian lights, and how to handle emergency pre-emption. The conflict monitor works alongside the traffic light controller, ensuring its operation doesn't lead to outcomes where people's safety are endangered, such as having green lights in multiple directions or having a pedestrian crossing enable while perpendicular to moving traffic. Any improper outcomes lead to the intersection going into a fail state. The traffic controller and conflict monitor directly control phase groups, which are just collections of lights that are green at the same time. This can include incoming traffic, such as north and south bound straight lights.

```
                Simulation Loop
                      │
                Intersection
                      │
        ┌─────────────┴─────────────┐
        │                           │
 Traffic Controller         Conflict Monitor
        │                           │
        └─────────────┬─────────────┘
                      │
                Phase Groups
                      │
               Signal Outputs
                      │
             ASCII Visualization
```

```
                 Simulation Loop
                        │
                        ▼
             Intersection Phase FSM
                        │
        ┌───────────────┼───────────────┐
        ▼               ▼               ▼
 Vehicle Detection  Pedestrian     Emergency
                    Requests       Pre-emption
        │               │               │
        └───────────────┼───────────────┘
                        ▼
               Phase Sequence FSMs
                        ▼
                Phase Group FSMs
                        ▼
              ASCII Visualization
```

## Finite State Machine

### FSM Hierarchy
The simulator uses hierarchical finite state machines to model the intersection. A top-level controller manages traffic phases and light sequences of each phase, while individual phase groups and traffic lights maintain their own state machines(eg. RED, YELLOW, GREEN, BLINKING_RED, and OFF). This separation mirrors how complex control systems decompose behavior into smaller, independently managed components.
```
Traffic Light Controller
        │
        ▼
Intersection Phase FSM
        │
        ▼
Phase Sequence FSM
        │
        ▼
Phase Group FSM
```

#### Intersection Phase FSM
1 -> North/South Left\
2 -> North/South Straight\
3 -> East/West Left\
4 -> East/West Straight\
*These numbers are determined by real-world traffic light standards. Odd number phases are usually for left turns while even number phases are usually for straight lights.

```
Phase 1 ─────────────► Phase 2
   ▲                     │
   │                     ▼
Phase 4 ◄──────────── Phase 3
```

#### Phase Sequence FSM
```
Green
  |
  ▼
Yellow
  |
  ▼
 RED
```

#### Phase Group FSM
- RED
- YELLOW
- GREEN
- BLINKING_RED
- OFF

## Project Structure

### traffic-controller/

│── intersection.py\
│── traffic_controller.py\
│── conflict_monitor.py\
│── signal_group.py\
│── pedestrian_light.py\
│── traffic_light.py\
│── constants.py\
│── main.py

## Design Decisions

One big design decision was on whether or not to use python considering how C or C++ is the industry standard. 
My focus was to focus on controller architecture and embedded design concepts rather than low-level language details. 
Python gives me the flexibility to make quick iterations while maintaining modularity by design. 
The focus on architecture and design means that the controller logic would remain largely the same, even in a different language.

Another decision was to use ASCII terminal art. 
This allowed me to get immediate visualization and feedback without requiring external graphics libraries.
Furthermore, this allowed me to directly wire visual elements to their locations and how they are displayed.

The decision to make sensors and the pedestrian buttons a simple boolean variable was to simplify unnecessary complexity.
For the button, a simple boolean variable would suffice to mimic a push rather than needing lines of code to read the voltage, which also means the simulation would need to also include voltage readings of every button.
Similarly, for the inductive loops, a boolean would suffice over having to mimic reading the frequency of an inductive loop.
Meanwhile, for the optical sensors, it means removing specific sensor specifications such as phase margins, range and detection margins, and bit-error rates from the simulation. 
These could affect how the high-frequency, coded infrared light of emergency vehicles are read.

The decision to separate configurable variables, such as configurable timing, into a separate constants file was to improve configurability and maintenance.
This allows for quickly accessing multiple variations of the intersection in size and timing without having to dig through code.
In real world operations, this would also allow for quick and intuitive changes to necessary parts of the code by people who don't need to necessarily understand it.
For example, if a port breaks, anyone can easily change the port in code. 

For the simulation, instead of having an user input system that allows the user to choose a specific event, the program prompts the user with each event before being able to move to the next tick. This decision for a bare-bones input system allowed for less focus on a full fledged user-program interaction system and quicker iteration of the traffic light controller without being bogged down by complicated wiring of inputs to simulated events. 

## What Was Modeled

- Traffic phases
- Signal groups
- Pedestrian crossings
- Timing plans
- Hardware-style signal inputs and outputs
- Conflict monitoring
- Vehicle detection
- Emergency vehicle pre-emption

## Simplifications

- Multiple intersections
- Adaptive traffic optimization
- Networked controllers

## Future improvements

- Write controller using C++ or C
- Multiple intersections
- GUI visualization
- Hardware support

## How to Run
```bash
git clone https://github.com/Fiszic/TrafficLightController.git
cd TrafficLightController
python main.py
```
