'''
Created on Apr 14, 2015

@author: mabuelanin
'''

from UDP import *
from Debug import *

button_value, type, key_number, btn = 4, 6, 7, 1

def but(s):  # Button Clicked         
    global button_value, type, key_number, btn   
#-------------------Button Down----------------------------                  
    if s[button_value] == 1:  # True                         
        #print "button (%d) DOWN" % (s[key_number])
        if(s[key_number] == 0):  # button 0                  
            udp("au")
            debug("Button 0 Pressed")
        if(s[key_number] == 1):  # button 1 
            udp("bu")
            debug("Button 1 Pressed")
        if(s[key_number] == 2):  # button 2                   
            udp("cu")
            debug("Button 2 Pressed")
        if(s[key_number] == 3):  # button 3                   
            udp("du")
            debug("Button 3 Pressed")
        if(s[key_number] == 4):  # button 4                   
            udp("eu")
            debug("Button 4 Pressed")
        if(s[key_number] == 5):  # button 5                   
            udp("fu")
            debug("Button 5 Pressed")
        if(s[key_number] == 6):  # button 6                   
            udp("gu")
            debug("Button 6 Pressed")
        if(s[key_number] == 7):  # button 7                   
            udp("hu")
            debug("Button 7 Pressed")
        if(s[key_number] == 8):  # button 8                   
            udp("iu")
            debug("Button 8 Pressed")
        if(s[key_number] == 9):  # button 9                   
            udp("ju")
            debug("Button 9 Pressed")
        if(s[key_number] == 10):  # button 10                   
            udp("ku")
            debug("Button 10 Pressed")
        if(s[key_number] == 11):  # button 11                  
            udp("lu")
            debug("Button 11 Pressed")
        if(s[key_number] == 12):  # button 12                  
            udp("mu")
            debug("Button 12 Pressed")
                     
# _______________________________________________________


    elif(s[button_value] == 0):  # Button Down                    
        #print "button (%d) UP" % (s[key_number])
        if(s[key_number] == 0):  # button 0                  
            udp("s")
            debug("Button 0 Released")
        if(s[key_number] == 1):  # button 1 
            udp("s")
            debug("Button 1 Released")
        if(s[key_number] == 2):  # button 2                   
            udp("s")
            debug("Button 2 Released")
        if(s[key_number] == 3):  # button 3                   
            udp("s")
            debug("Button 3 Released")
        if(s[key_number] == 4):  # button 4                   
            udp("s")
            debug("Button 4 Released")
        if(s[key_number] == 5):  # button 5                   
            udp("s")
            debug("Button 5 Released")
        if(s[key_number] == 6):  # button 6                   
            udp("s")
            debug("Button 6 Released")
        if(s[key_number] == 7):  # button 7                   
            udp("s")
            debug("Button 7 Released")
        if(s[key_number] == 8):  # button 8                   
            udp("s")
            debug("Button 8 Released")
        if(s[key_number] == 9):  # button 9                   
            udp("s")
            debug("Button 9 Released")
        if(s[key_number] == 10):  # button 10                   
            udp("s")
            debug("Button 10 Released")
        if(s[key_number] == 11):  # button 11                  
            udp("s")
            debug("Button 11 Released")
        if(s[key_number] == 12):  # button 12                  
            udp("s")
            debug("Button 12 Released")
        

#---------------------------------------------------------
#-----------------------BUTTON EVENT--------------------    