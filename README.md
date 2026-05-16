# Solar System in Python

A solar system simulation project built with Python and turtle graphics.

This project uses object-oriented programming and basic gravity physics to simulate planets orbiting around the sun.

## Features
* Object-oriented design
* Planet orbit simulation
* Basic gravity physics
* Real-time animation with turtle graphics
* Sun, planet, and moon system

## Tools
* Python
* Turtle Graphics
* Object-Oriented Programming
* Basic Physics Simulation

## Physics Concepts
### Velocity Update
From the universal gravitation formula:

$$
F = G\frac{Mm}{r^2}
$$

and Newton's second law:

$$
F = ma
$$

we can get the acceleration:

$$
a = G\frac{M}{r^2}
$$

Then, we use the velocity update formula:

$$
v' = v + a\Delta t
$$

to calculate the planet's new velocity.

### Position Update
Using the position update formula:

$$
x' = x + v\Delta t
$$

we can calculate the planet's new position.

## Program Structure
```text
Solar_System.py

├── Sun
│   ├── Store sun data
│   ├── Create sun graphics
│   └── Calculate volume, surface area, and density
│
├── Planet
│   ├── Store planet data
│   ├── Set velocity and position
│   ├── Update planet movement
│   └── Draw planets with turtle graphics
│
├── Moon
│   ├── Store moon data
│   ├── Simulate moon movement
│   └── Draw moon orbit
│
├── SolarSystem
│   ├── Manage all celestial bodies
│   ├── Calculate gravitational force
│   ├── Update velocity and position
│   └── Control animation
│
└── creatSSandAnimate()
    ├── Create the sun and planets
    ├── Initialize the solar system
    ├── Run animation loop
    └── Start simulation
```
## Results


## How to Run
```bash
python Solar_System.py
```
