#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import TouchSensor, ColorSensor
from pybricks.parameters import Port, Color
from pybricks.tools import wait
from pybricks.media.ev3dev import SoundFile, Font

# Create the brick connection.
ev3 = EV3Brick()
# Set font.
font = Font(size=16, bold=True)
ev3.screen.set_font(font)

# Initialize Color sensor.
colorSensor = ColorSensor(Port.S3)

# Adjust volume.
ev3.speaker.set_volume(70)

# Colors dictionary.
colors = {
    Color.BLACK : SoundFile.BLACK,
    Color.BLUE : SoundFile.BLUE,
    Color.GREEN : SoundFile.GREEN,
    Color.YELLOW : SoundFile.YELLOW,
    Color.RED : SoundFile.RED,
    Color.WHITE : SoundFile.WHITE,
    Color.BROWN : SoundFile.BROWN
}

# Test colors.
counter = 0
while counter < 5:
    wait(10)
    color = colorSensor.color()
    r, g, b = colorSensor.rgb()
    ev3.screen.print('r=', r, 'g=', g, 'b=', b, '(%)')
    ev3.screen.print('ambient', colorSensor.ambient(), '%')
    ev3.screen.print('reflection', colorSensor.reflection(), '%')
    if color != None:
        counter = counter + 1
        ev3.speaker.play_file(colors.get(color, 'unknown'))

ev3.speaker.play_file(SoundFile.GOODBYE)