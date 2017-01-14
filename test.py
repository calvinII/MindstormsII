#!/usr/bin/env python3

from time import sleep
import ev3dev.ev3 as ev3
import threading

ev3.Sound.speak('Welcome to the E V 3 dev project!').wait()

# us_sensor = ev3.UltrasonicSensor()
#
# while True:
#     print(us_sensor.distance_centimeters)
#     sleep(0.1)
