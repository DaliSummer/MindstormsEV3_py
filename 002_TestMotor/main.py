#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor
from pybricks.parameters import Port

# Initialize the EV3 Brick.
ev3 = EV3Brick()

# Initialize a motor at port B.
motorB = Motor(Port.B)
# Initialize a motor at port C.
motorC = Motor(Port.C)

# Play a beep sound.
ev3.speaker.beep()

# Run the motor up to 500 degrees per second. To a target angle of 180 degrees.
motorB.run_target(100, 180)

# Play another beep sound.
ev3.speaker.beep(frequency=5000, duration=500)

# Run the motor up to 100 degrees per second. To a target angle of 270 degrees.
motorC.run_target(500, 270)

# Run the motor and continue the program.
motorB.run_target(1000, -500, wait=False)
# Run the motor and wait it to reach the target before continuing the program. 
motorC.run_target(1000, -500, wait=True)
