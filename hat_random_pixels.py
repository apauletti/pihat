#!/usr/bin/env python
# this script will display random colors for a random individual pixel on the Pi HAT
from sense_hat import SenseHat
sense = SenseHat()
import random
import time

x = random.randint(0,7)
y = random.randint(0,7)
r = random.randint(0,255)
g = random.randint(0,255)
b = random.randint(0,255)

sense.set_pixel(x, y, (r, g, b))

time.sleep(1)
sense.clear()
