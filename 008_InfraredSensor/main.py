#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import InfraredSensor
from pybricks.parameters import Port, Button
from pybricks.tools import wait
from pybricks.media.ev3dev import SoundFile, Font

# Create the brick connection.
ev3 = EV3Brick()

# Set Font.
print_font = Font(size=16, bold=True)
ev3.screen.set_font(print_font)

# Initialize IR sensor.
ir = InfraredSensor(Port.S4)

# Adjust voice.
ev3.speaker.set_speech_options('en', 'f3', 25, 50)
ev3.speaker.set_volume(50)

# Check a pressed button and name it.
while True:
    buttons = ir.buttons(1)
    wait(10)
    if Button.BEACON in buttons:
        ev3.speaker.say('beacon')
        break
    
    elif Button.LEFT_UP in buttons and Button.RIGHT_UP in buttons:
        ev3.speaker.play_file(Sound.UP)
    elif Button.LEFT_DOWN in buttons and Button.RIGHT_DOWN in buttons:
        ev3.speaker.play_file(Sound.DOWN)
    elif Button.LEFT_UP in buttons and Button.LEFT_DOWN in buttons:
        ev3.speaker.say('left')
    elif Button.RIGHT_UP in buttons and Button.RIGHT_DOWN in buttons:
        ev3.speaker.say('right')

    elif Button.LEFT_UP in buttons:
        ev3.speaker.play_file(Sound.LEFT)
        ev3.speaker.play_file(Sound.UP)
    elif Button.LEFT_DOWN in buttons:
        ev3.speaker.play_file(Sound.LEFT)
        ev3.speaker.play_file(Sound.DOWN)
    elif Button.RIGHT_UP in buttons:
        ev3.speaker.play_file(Sound.RIGHT)
        ev3.speaker.play_file(Sound.UP)
    elif Button.RIGHT_DOWN in buttons:
        ev3.speaker.play_file(Sound.RIGHT)
        ev3.speaker.play_file(Sound.DOWN)

ev3.speaker.say('come to me')

dist = 100
while dist > 30:
    wait(10)
    dist = ir.distance()
    ev3.screen.print('Distance: ', dist, 'mm')

ev3.speaker.say('come to me on channel 1')

dist = 100
angle = 0
while dist > 10:
    wait(10)
    dist, angle = ir.beacon(1)
    ev3.screen.print('Distance: ', dist*2, 'mm')
    ev3.screen.print('Angle: ', angle, 'deg')

ev3.speaker.say('last try, use channel 1')

while True:
    buttons = ir.keypad()
    wait(10)

    if Button.LEFT_UP in buttons and Button.RIGHT_UP in buttons and Button.RIGHT_DOWN in buttons:
        ev3.speaker.play_file(Sound.GOODBYE)
        break
    elif Button.LEFT_UP in buttons and Button.RIGHT_UP in buttons:
        ev3.speaker.play_file(Sound.UP)
    elif Button.LEFT_DOWN in buttons and Button.RIGHT_DOWN in buttons:
        ev3.speaker.play_file(Sound.DOWN)
    elif Button.LEFT_UP in buttons and Button.LEFT_DOWN in buttons:
        ev3.speaker.play_file(Sound.LEFT)
    elif Button.RIGHT_UP in buttons and Button.RIGHT_DOWN in buttons:
        ev3.speaker.play_file(Sound.RIGHT)

    elif Button.LEFT_UP in buttons:
        ev3.speaker.play_file(Sound.LEFT)
        ev3.speaker.play_file(Sound.UP)
    elif Button.LEFT_DOWN in buttons:
        ev3.speaker.play_file(Sound.LEFT)
        ev3.speaker.play_file(Sound.DOWN)
    elif Button.RIGHT_UP in buttons:
        ev3.speaker.play_file(Sound.RIGHT)
        ev3.speaker.play_file(Sound.UP)
    elif Button.RIGHT_DOWN in buttons:
        ev3.speaker.play_file(Sound.RIGHT)
        ev3.speaker.play_file(Sound.DOWN)
