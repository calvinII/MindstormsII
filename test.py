#!/usr/bin/env python3

from time import sleep
import ev3dev.ev3 as ev3

btn = ev3.Button()

print("starting! ")
while True:
    if btn.any():    # Checks if any button is pressed.
        print("Wow")
        exit()
    else:
        sleep(0.01)  # Check for button press every 0.01 second

