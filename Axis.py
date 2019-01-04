'''
Created on Apr 14, 2015

@author: mabuelanin
'''

from UDP import *
from Debug import *
from map import *

axis_value, type, key_number, ax = 5, 6, 7, 2


def axis(s):  # Axis Pressed
    global button_value, axis_value, type, key_number, btn, ax  
    # print "axis (%d) value (%d)" % (s[7],s[5])

#----------HAT--------------------------------------
    if (s[axis_value] == 128 and s[key_number] == 5):  # HAT UP
        udp("HF")
        debug("HAT Forward") 
    elif (s[axis_value] == 127 and s[key_number] == 5):  # HAT DOWN
        udp("HB")
        debug("HAT Backward")
    elif (s[axis_value] == 128 and s[key_number] == 4):  # LEFT HAT
        udp("HL")
        debug("HAT left")
    elif (s[axis_value] == 127 and s[key_number] == 4):  # Right HAT
        udp('HR')
        debug("HAT right")
    elif (s[axis_value] == 0 and (s[key_number] == 4 or s[key_number] == 5)):  # Right HAT
        udp('HS'+chr(48))
        debug("HAT Stopped")
#-----------------------HAT END--------------------


#---------Main Analog-----------------------------------            
    if ((s[axis_value] < 253 and s[axis_value] > 128) and s[key_number] == 1):  # forward
        udp('MF'+chr(map(s[axis_value], 253, 128, 0, 255)))
        debug("Main analog Forward")
    elif ((s[axis_value] < 127 and s[axis_value] > 1) and s[key_number] == 1):  # backward
        udp('MB'+chr(map(s[axis_value], 1, 127, 0, 255)))
        debug("Main analog Backward")
    elif ((s[axis_value] < 235 and s[axis_value] > 128) and s[key_number] == 0):  # left
        udp('ML'+chr(map(s[axis_value], 253, 128, 0, 255)))
        debug("Main analog Left")
    elif ((s[axis_value] < 127 and s[axis_value] > 1) and s[key_number] == 0):  # right
        udp('MR'+chr(map(s[axis_value], 1, 127, 0, 255)))
        debug("Main analog Right")
    elif (s[axis_value] == 0 and (s[axis_value] == 1 or s[axis_value] == 0)):
        udp('MS'+chr(48))
        debug("Main analog Originated")
#-----------------------AXIS 3 END--------------------

#---------Rotate Analog-----------------------------------            
    if ((s[axis_value] < 253 and s[axis_value] > 128) and s[key_number] == 2):  # Left
        udp('RL'+chr(map(s[axis_value], 253, 128, 0, 255)))
        debug("Rotate Left")
    elif ((s[axis_value] < 127 and s[axis_value] > 0) and s[key_number] == 2):  # Right
        udp('RR'+chr(map(s[axis_value], 1, 127, 0, 255)))
        debug("Rotate Right")
    elif (s[axis_value] == 0 and s[key_number] == 2):
        udp('RS'+chr(48))
        debug("Rotate Stopped")
#-----------------------Rotate Analog END--------------------


#---------Secondary Analog-----------------------------------            
    if ((s[axis_value] < 254 and s[axis_value] > 128) and s[key_number] == 3):  # forward
        udp("SF"+str(chr(map(s[axis_value], 253, 128, 0, 255))))
        #print "SF"+str(chr(map(s[axis_value], 253, 128, 0, 255)))
        debug("Secondary Forward")
    
    elif ((s[axis_value] < 127 and s[axis_value] > 0) and s[key_number] == 3):  # backward
        udp('SB'+chr(map(s[axis_value], 1, 127, 0, 255)))
        debug("Secondary Backward")
    elif (s[axis_value] == 0 and s[7] == 3):
        udp('SS'+chr(48))
        debug("Secondary Stopped")
#-----------------------Secondary Analog END--------------------
