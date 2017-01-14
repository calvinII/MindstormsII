from time import sleep
import ev3dev.ev3 as ev3

us_sensor = ev3.UltrasonicSensor()

while True:
    print(us_sensor.distance_centimeters)
    sleep(0.1)