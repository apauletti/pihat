#!/usr/bin/env python
# this script will define colors for a scrolling message on the Pi HAT
from sense_hat import SenseHat
sense = SenseHat()

# use RGB values to define colors
yellow = (255, 255, 0)
blue = (0, 0, 255)

speed = 0.05

message = "Hello World!"

sense.show_message(message, speed, text_colour=yellow, back_colour=blue)

sense.clear()
