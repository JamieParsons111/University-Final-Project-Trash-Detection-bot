import time
import nxt.motor
import nxt.locator
import nxt.sensor
import nxt.sensor.generic


with nxt.locator.find() as b:
    #Find the sensor connected to port 4.
    mysensor = b.get_sensor(nxt.sensor.Port.S4)
    # Read the sensor in a loop (until interrupted).
    print("Use Ctrl-C to interrupt")
    while True:
        distance_cm = mysensor.get_sample()
        mymotor = b.get_motor(nxt.motor.Port.A)
        mymotor2 = b.get_motor(nxt.motor.Port.C)
        mymotor.run(100)
        mymotor2.run(100)

   
        if distance_cm < 50:
            print("Too close")
            b.play_tone(440, 250) 
            mymotor.brake()
            mymotor2.brake()
            break
