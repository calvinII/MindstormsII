#!/usr/bin/env python3

import ev3dev.ev3 as ev3

motorA = ev3.LargeMotor(ev3.OUTPUT_A)
motorD = ev3.LargeMotor(ev3.OUTPUT_D)

motorA.reset()
motorD.reset()
motorA.run_to_rel_pos(position_sp=1080, speed_sp=900, stop_action="hold")
motorD.run_to_rel_pos(position_sp=-1080, speed_sp=900, stop_action="hold")

sleep(10)