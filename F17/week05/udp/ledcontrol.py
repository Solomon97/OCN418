# UDP demo
# works with ledserver.py
#
# Stanley H.I. Lio
# hlio@hawaii.edu
import socket


IP = '192.168.2.215'
PORT = 50006

sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

while True:
    m = input('on or off? ')
    if m in ['on','off']:
        print(m)
        sock.sendto(m.encode(),(IP,PORT))
    else:
        print('it\'s beyond my paygrade')
