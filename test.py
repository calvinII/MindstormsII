#!/usr/bin/env python3

from time import sleep
import ev3dev.ev3 as ev3
import threading

class Head:
    def __init__(self):
        self.__distance = 100000
        self.__us_sensor = ev3.UltrasonicSensor()
        assert self.__us_sensor.connected
        self.__read_thread = threading.Thread(target=self.__read_sensor())
        self.__read_thread.setDaemon(True)
        self.__read_thread.start()
        self.__action_thread = threading.Thread(target=self.__action())
        self.__action_thread.setDaemon(True)
        self.__action_thread.start()

    def __read_sensor(self):
        print("Reading Sensors")
        while True:
            self.__distance = self.__us_sensor.distance_centimeters
            sleep(0.1)

    def __action(self):
        print("Checking Sensor")
        while True:
            if self.__distance <= 100:
                print(self.__distance)
            sleep(0.1)


head = Head()
sleep(100)

