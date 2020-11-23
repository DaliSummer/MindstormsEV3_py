#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, InfraredSensor
from pybricks.parameters import Port, Stop, Direction, Button
from pybricks.tools import wait
from pybricks.media.ev3dev import Font

def printMotor(motor, screen):
    screen.print('speed: ', motor.speed(), 'deg/s')
    screen.print('angle: ', motor.angle(), 'deg')
    return

def waiter(ir_sensor):
    while True:
        btn = ir_sensor.buttons(1)
        wait(150)
        if Button.LEFT_UP in btn:
            return

big_font = Font(size=16, bold=True)
ev3 = EV3Brick()
ev3.screen.set_font(big_font)

# Initialize IR sensor
ir = InfraredSensor(Port.S4)

# Initialize motors
motorB = Motor(port=Port.B, positive_direction=Direction.CLOCKWISE, gears=None)
motorC = Motor(port=Port.C, positive_direction=Direction.COUNTERCLOCKWISE, gears=[36, 12])

ev3.screen.print('=Motor C=')
printMotor(motorC, ev3.screen)
waiter(ir)

ev3.screen.print('=run 500=')
motorC.run(500)
waiter(ir)
printMotor(motorC, ev3.screen)
motorC.stop()
waiter(ir)

ev3.screen.print('=Motor B=')
printMotor(motorB, ev3.screen)
waiter(ir)

ev3.screen.print('=run 500=')
motorB.run(500)
waiter(ir)
printMotor(motorB, ev3.screen)
motorB.stop()
waiter(ir)

ev3.screen.print('=run brake=')
motorB.run_time(speed=500, time=3000, then=Stop.BRAKE, wait=True)
waiter(ir)

ev3.screen.print('=run coast=')
motorB.run_time(speed=500, time=3000, then=Stop.COAST, wait=True)
waiter(ir)

ev3.screen.print('=run hold=')
motorB.run_time(speed=500, time=3000, then=Stop.HOLD, wait=True)
waiter(ir)

ev3.screen.print('=reset angle 0=')
motorB.reset_angle(0)
printMotor(motorB, ev3.screen)
waiter(ir)

ev3.screen.print('=angle 180=')
motorB.run_angle(speed=500, rotation_angle=180, then=Stop.HOLD, wait=True)
printMotor(motorB, ev3.screen)
waiter(ir)

ev3.screen.print('=run target 90=')
motorB.run_target(speed=500, target_angle=90, then=Stop.HOLD, wait=True)
printMotor(motorB, ev3.screen)
waiter(ir)

ev3.screen.print('=angle 90=')
motorB.run_angle(speed=500, rotation_angle=90, then=Stop.HOLD, wait=True)
printMotor(motorB, ev3.screen)
waiter(ir)

ev3.screen.print('=track target 90=')
motorB.track_target(target_angle=90)
waiter(ir)

ev3.screen.print('=until stalled=')
motorB.run_until_stalled(15, then=Stop.COAST, duty_limit=10)
printMotor(motorB, ev3.screen)
waiter(ir)

ev3.screen.print('=duty 100=')
motorB.dc(100)
waiter(ir)
printMotor(motorB, ev3.screen)
motorB.stop()
waiter(ir)

ev3.screen.print('=duty -100=')
motorB.dc(-100)
waiter(ir)
printMotor(motorB, ev3.screen)
motorB.stop()
waiter(ir)