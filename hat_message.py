#!/usr/bin/env python
# this script will show a scrolling message on the Pi HAT
from sense_hat import SenseHat
sense = SenseHat()

# send the text Hello World! to the show_message() frunction
sense.show_message("Hello World!")
