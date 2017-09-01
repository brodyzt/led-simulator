#!/usr/bin/python
# -*- coding: utf-8 -*-

#
# -----------------------------------------------------
# File        fading.py
# Authors     David Ordnung
# License     GPLv3
# Web         http://dordnung.de/raspberrypi-ledstrip/
# -----------------------------------------------------
#
# Copyright (C) 2014-2017 David Ordnung
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>
#


# This script needs running pigpio (http://abyz.co.uk/rpi/pigpio/)


###### CONFIGURE THIS ######

# The Pins. Use Broadcom numbers.
RED_PIN = "Red"
GREEN_PIN = "Green"
BLUE_PIN = "Blue"

# Number of color changes per step (more is faster, less is slower).
# You also can use 0.X floats.
STEPS = 1

###### END ######




import os
import sys
import termios
import tty
import time
from thread import start_new_thread
import requests, json


def setLights(state):
    if(state == "ON"):
        payload = {
            "red": 255,
            "green": 255,
            "blue": 255
        }
    else:
        payload = {
            "red": 0,
            "green": 0,
            "blue": 0
        }

    headers = {"content-type": "application/json"}
    url = "http://10.0.1.105:5000/color"
    put = requests.put(url, data=json.dumps(payload), headers=headers)


state = "OFF"

setLights(state)

while True:
    if state == "OFF":
        setLights("ON")
        state = "ON"

    else:
        setLights("OFF")
        state = "OFF"
    time.sleep(1)
