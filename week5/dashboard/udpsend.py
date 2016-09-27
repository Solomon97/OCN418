import socket
from random import random


UDP_IP = '127.0.0.1'
UDP_PORT = 9999

sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

for i in range(1,13):
    #sock.sendto(bytearray('1,3.14',encoding='ascii'),(UDP_IP,UDP_PORT))
    sock.sendto(bytearray('{},{}'.format(i,25 + 5*(random()-0.5)),\
                          encoding='ascii'),(UDP_IP,UDP_PORT))
