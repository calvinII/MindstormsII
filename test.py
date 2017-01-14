#!/usr/bin/env python3

from time import sleep
import ev3dev.ev3 as ev3
import threading

class Head:
    def __init__(self):
        self.__distance = None
        self.__us_sensor = ev3.UltrasonicSensor()
        self.thread = threading.Thread(target=self.__read_sensor())
        self.thread.start()
        self.thread = threading.Thread(target=self.__action())
        self.thread.start()

    def __read_sensor(self):
        while True:
            self.__distance = self.__us_sensor.distance_centimeters()
            sleep(0.001)

    def __action(self):
        while True:
            if self.__distance <= 100:
                print(self.__distance)
            sleep(0.001)


head = Head()
sleep(100)

