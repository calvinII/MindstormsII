#!/usr/bin/env python3

from time import sleep
import ev3dev.ev3 as ev3
import threading


class Head(threading.Thread):
    def __init__(self, bite_distance=400):
        threading.Thread.__init__(self)
        self.daemon = True
        self.__distance = 100000
        self.__bite_distance = bite_distance
        self.__us_sensor = ev3.UltrasonicSensor()
        self.__head_motor = ev3.MediumMotor('outB')
        self.__head_motor.reset()
        assert self.__us_sensor.connected

    def __bite(self):
        self.__head_motor.polarity = 'inversed'
        self.__head_motor.run_to_abs_pos(position_sp=180, speed_sp=900, stop_action='hold')
        sleep(1)
        self.__head_motor.polarity = 'inversed'
        self.__head_motor.run_to_abs_pos(position_sp=0, speed_sp=500, stop_action='coast')

    def run(self):
        while True:
            self.__distance = self.__us_sensor.distance_centimeters
            if self.__distance <= self.__bite_distance:
                self.__bite()
                # Warten bis der Kopf eingezogen ist
                sleep(2)
            sleep(0.01)


head = Head()
head.start()
while True:
    print("hmmmm hmmmmh")
    sleep(2)


