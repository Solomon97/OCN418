# Move a gauge to a predetermined position.
#
# ID is an integer in [1,20]
# value is a number from [0,100]
#
# Stanley H.I. Lio
# hlio@hawaii.edu
import socket


IP = '192.168.2.200'
PORT = 9999

sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

# Format: yourID,value
# Your ID can be an integer in [1,20]
# ID = 1, value = 42:
m = '1,42'

sock.sendto(bytearray(m,encoding='ascii'),(IP,PORT))
