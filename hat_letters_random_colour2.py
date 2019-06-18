#!/usr/bin/env python
# this script will display letters with random colors on the Pi HAT
from sense_hat import SenseHat
import time
import random
sense = SenseHat()
# assign a random integer between 0 and 255 to a variable named r
r1 = random.randint(0,255)
g1 = random.randint(0,255)
b1 = random.randint(0,255)
r2 = random.randint(0,255)
g2 = random.randint(0,255)
b2 = random.randint(0,255)
r3 = random.randint(0,255)
g3 = random.randint(0,255)
b3 = random.randint(0,255)

sense.show_letter("H",(r1, g1, b1))
time.sleep(1)
sense.show_letter("i", (r2, g2, b2))
time.sleep(1)
sense.show_letter("!", (r3, g3, b3))
time.sleep(1)

sense.clear()
