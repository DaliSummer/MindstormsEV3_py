#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.parameters import Button
from pybricks.tools import wait
from pybricks.media.ev3dev import Font

# Load Font
big_font = Font(size=24, bold=True)

# Initialize the EV3
ev3 = EV3Brick()

# Print Battery parameters
ev3.screen.set_font(big_font)
ev3.screen.print('Voltage: \n', ev3.battery.voltage(), ' mV')
ev3.screen.print('Current: \n', ev3.battery.current(), ' mA')

while True:
    buttons = ev3.buttons.pressed()
    wait(150)
    if Button.UP in buttons:
        break