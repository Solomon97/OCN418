import socket
from random import random


IP = '192.168.2.200'
PORT = 9999

sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

for i in range(1,21):
    #sock.sendto(bytearray('1,3.14',encoding='ascii'),(UDP_IP,UDP_PORT))
    sock.sendto(bytearray('{},{}'.format(i,50 + 20*(random()-0.5)),\
                          encoding='ascii'),(IP,PORT))
