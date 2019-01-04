'''
Created on Apr 14, 2015

@author: mabuelanin
'''
"""
Bytes:
4> button value : 1=DOWN , 0=UP
5> axes value
6> 129=but,130=ax || 1=ax,2=but
7> axis OR button Number 

button_value =4
axis_value=5
type= 6
key_number=7
btn=1
ax=2
"""



debugging = True


def debug(direction):
    global debugging
    if(debugging):
        print direction