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
