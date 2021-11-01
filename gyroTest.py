#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
from time import sleep


# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.


# Create your objects here.
ev3 = EV3Brick()
#left_motor = Motor(Port.B)
#right_motor = Motor(Port.D)
#servo = Motor(Port.C)
gyro = GyroSensor(Port.S1)


#gyro.mode='GYRO-ANG'

#units = gyro.units()
#robot = DriveBase(left_motor, right_motor)
# Write your program here.
ev3.speaker.beep()
#left_motor.run_time(1000, 5000, wait=False)
#right_motor.run_time(1000, 5000,)

while True:
    angle = gyro.angle()
    print(str(angle))
    sleep(0.5)
#ActAngle = gyro.angle()
#Desired_angle = ActAngle * -1
#servo.run_target(100, then=Stop.HOLD)
