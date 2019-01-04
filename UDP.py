'''
Created on Apr 14, 2015

@author: mabuelanin
'''
UDP_IP = "192.168.1.10"
UDP_PORT = 11000
#UDP_PORT = 8888
import socket
socket_state=True


sock = socket.socket(socket.AF_INET,  # Internet

                     socket.SOCK_DGRAM)  # UDP


def udp(c):
    global socket_state
    if(socket_state):
        sock.sendto(c.lower(), (UDP_IP, UDP_PORT))
        print "UDP: ",c.lower(),"Sent"