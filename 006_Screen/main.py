#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.parameters import Button, Color
from pybricks.tools import wait
from pybricks.media.ev3dev import Font
from pybricks.media.ev3dev import Image, ImageFile

# It takes some time for fonts to load from file, so it is best to only
# load them once at the beginning of the program like this:
tiny_font = Font(size=6)
big_font = Font(size=24, bold=True)
chinese_font = Font(size=24, lang='zh-cn')
ukrainian_font = Font(size=20, lang='uk')

# Initialize the EV3
ev3 = EV3Brick()

# Say hello
ev3.screen.print('Hello!')
# Say tiny hello
ev3.screen.set_font(tiny_font)
ev3.screen.print('hello')
# Say big hello
ev3.screen.set_font(big_font)
ev3.screen.print('HELLO')
# Say Chinese hello
ev3.screen.set_font(chinese_font)
ev3.screen.print('你好')
# Say Ukrainian hello
ev3.screen.set_font(ukrainian_font)
ev3.screen.print('Привіт')

while True:
    buttons = ev3.buttons.pressed()
    wait(150)
    if Button.UP in buttons:
        break

# Clean screen
ev3.screen.clear()

# Print screen size
ev3.screen.set_font(big_font)
ev3.screen.print('SIZE: ', ev3.screen.width, 'x', ev3.screen.height)

while True:
    buttons = ev3.buttons.pressed()
    wait(150)
    if Button.UP in buttons:
        break

# Clean screen
ev3.screen.clear()

# Draw text
ev3.screen.draw_text(ev3.screen.width/2-30, ev3.screen.height/2-12, "+++", Color.WHITE, Color.BLACK)

while True:
    buttons = ev3.buttons.pressed()
    wait(150)
    if Button.UP in buttons:
        break

# Clean screen
ev3.screen.clear()

# Create Image
img = Image(ImageFile.EV3_ICON)
# Show an image
ev3.screen.load_image(img)

while True:
    buttons = ev3.buttons.pressed()
    wait(150)
    if Button.UP in buttons:
        break

# Clean screen
ev3.screen.clear()

# Draw image from file
ev3.screen.draw_image((ev3.screen.width-100)/2, (ev3.screen.height-100)/2, "../data/robot_icon.png", None)

while True:
    buttons = ev3.buttons.pressed()
    wait(150)
    if Button.UP in buttons:
        break

# Clean screen
ev3.screen.clear()

# Draw Box
ev3.screen.draw_box(0, 0, ev3.screen.width, ev3.screen.height, 15, True, Color.BLACK)
# Draw Circle
ev3.screen.draw_circle(ev3.screen.width/2, ev3.screen.height/2, ev3.screen.height/2-15, False, Color.WHITE)
# Draw Pixels
ev3.screen.draw_pixel(ev3.screen.width/2, ev3.screen.height/2, Color.WHITE)
ev3.screen.draw_pixel(ev3.screen.width/2-1, ev3.screen.height/2, Color.WHITE)
ev3.screen.draw_pixel(ev3.screen.width/2, ev3.screen.height/2-1, Color.WHITE)
ev3.screen.draw_pixel(ev3.screen.width/2+1, ev3.screen.height/2, Color.WHITE)
ev3.screen.draw_pixel(ev3.screen.width/2, ev3.screen.height/2+1, Color.WHITE)
# Draw Line
ev3.screen.draw_line(0, 50, ev3.screen.width, 50, 10, Color.WHITE)

while True:
    buttons = ev3.buttons.pressed()
    wait(150)
    if Button.UP in buttons:
        break

# Save screen
ev3.screen.save("../data/printscreen.png")