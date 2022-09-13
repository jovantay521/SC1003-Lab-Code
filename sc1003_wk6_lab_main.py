# Coding Exercise 5b

# imports
from sense_hat import SenseHat
sense = SenseHat()
sense.set_rotation(180)

from sc1003_wk6_lab_module import get_colour

# main 
r_int = get_colour("red")
g_int = get_colour("green")
b_int = get_colour("blue")
msg_colour = (r_int, g_int, b_int)
sense.show_message("I got it!, text_colour=msg_colour")
