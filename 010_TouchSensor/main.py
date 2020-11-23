#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import TouchSensor
from pybricks.parameters import Port
from pybricks.tools import wait

# Create the brick connection.
ev3 = EV3Brick()

# Initialize Touch sensor.
touchSensor = TouchSensor(Port.S1)

# Adjust voice.
ev3.speaker.set_speech_options('en', 'f3', 25, 50)
ev3.speaker.set_volume(50)

# Test touches.
counter = 0
while counter < 3:
    wait(10)
    if touchSensor.pressed() == True:
        counter = counter + 1
        ev3.speaker.say("Don't touch me")

ev3.speaker.say("Good buy!")
