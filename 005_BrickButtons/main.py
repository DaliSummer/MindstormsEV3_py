#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.parameters import Button
from pybricks.tools import wait

# Create the brick connection.
ev3 = EV3Brick()

# Adjust voice.
ev3.speaker.set_speech_options('en', 'm7', 15, 95)

# Check a pressed button and name it.
while True:
    buttons = ev3.buttons.pressed()
    if Button.CENTER in buttons:
        ev3.speaker.say('center')
        break
    elif Button.UP in buttons:
        ev3.speaker.say('up')
    elif Button.DOWN in buttons:
        ev3.speaker.say('down')
    elif Button.LEFT in buttons:
        ev3.speaker.say('left')
    elif Button.RIGHT in buttons:
        ev3.speaker.say('right')
    # Wait for 100 ms.
    wait(100)