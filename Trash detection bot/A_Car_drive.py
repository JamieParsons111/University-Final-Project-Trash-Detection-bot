#!/usr/bin/python3
"""NXT-Python tutorial: find the brick."""
import time
import nxt.sensor
import nxt.motor 
from nxt.motor import Mode, Port,RegulationMode, RunState
import nxt.locator
import nxt.sensor.generic
import sys

# Find a brick.
with nxt.locator.find() as b:
    # Once found, print its name.
    print("Found brick:", b.get_device_info()[0])
    # And play a recognizable note.
    b.play_tone(440, 250)   

    mysensor = b.get_sensor(nxt.sensor.Port.S4)
    # Read the sensor in a loop (until interrupted).
    end = ''

    while True:
        motor = b.get_motor(nxt.motor.Port.A)
        motor2 = b.get_motor(nxt.motor.Port.C)
        both = nxt.motor.SynchronizedMotors(motor, motor2, 0)
        l_both=nxt.motor.SynchronizedMotors(motor, motor2, 100)
        r_both=nxt.motor.SynchronizedMotors(motor2, motor, 100)
        print("Hello there")
        distance_cm = mysensor.get_sample()
        print(distance_cm)
        
        while mysensor.get_sample()>40:

            both.run(100)
            time.sleep(4)
            l_both.turn (100,300,False)
            both.run(100)


        else:
            print(distance_cm)
            print("Uh oh")
            both.turn(-100, 360, False)
            r_both.turn(100,300,False)
            continue
          
        
            
        
        
            
        

       
      



    