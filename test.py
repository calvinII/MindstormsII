#!/usr/bin/env python3

from time import sleep
import ev3dev.ev3 as ev3
import threading


class Head(threading.Thread):
    def __init__(self):
        super().__init__()
        self.daemon = True
        self.start()
        self.__distance = 100000
        self.__us_sensor = ev3.UltrasonicSensor()
        assert self.__us_sensor.connected

    def run(self):
        while True:
            self.__distance = self.__us_sensor.distance_centimeters
            if self.__distance <= 100:
                print("AAAAAhhh {}".format(self.__distance))
            sleep(0.01)

head = Head()
while True:
    print("hmmmm")
    sleep(2)


