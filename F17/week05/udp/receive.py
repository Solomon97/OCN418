# UDP demo (Rx)
#
# Stanley H.I. Lio
# hlio@hawaii.edu
import socket


IP = ''
PORT = 5005

sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
sock.bind((IP,PORT))

print('Listening...')
while True:
    data,addr = sock.recvfrom(1024)
    print('Received: ' + data.decode())
