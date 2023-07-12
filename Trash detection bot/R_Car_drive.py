import nxt.sensor
import nxt.motor 
from nxt.motor import *
import nxt.locator
import nxt.sensor.generic
import sys

with nxt.locator.find() as b:
    # Once found, print its name.
    print("Found brick:", b.get_device_info()[0])
    # And play a recognizable note.
    b.play_tone(440, 250)  

    motor = b.get_motor(nxt.motor.Port.A)
    motor2 = b.get_motor(nxt.motor.Port.C)

    both = nxt.motor.SynchronizedMotors(motor, motor2, 0)
    l_both=nxt.motor.SynchronizedMotors(motor, motor2, 100)
    r_both=nxt.motor.SynchronizedMotors(motor2, motor, 100)
    print("ready")
    key = ''
    while key != 'q':
        key = sys.stdin.read(1)
        if key == 'w':
            print("Forwards")
            both.turn(100,360,False)
        elif key == 's':
            print("Backwards")
            both.turn(-100, 360, False)
        elif key == 'a':
            print( "Left")
            l_both.turn (100,300,False)
        elif key == 'd':
            print ("Right")
            r_both.turn(100,300,False)