import sys
import socket
from macpath import join
from Debug import *
from Axis import *
from Button import *
from map import *

debugging = True
sock = False
                     
# Open the js0 device as if it were a file in read mode.
pipe = open('/dev/input/js0', 'r')

# Create an empty list to store read characters.
msg = []

while 1:
    for char in pipe.read(1):
        msg += [ord(char)]
        if len(msg) == 8:
            if msg[type] == 1:
                but(msg)
            elif msg[type] == 2:
                axis(msg)
                   
            msg = []