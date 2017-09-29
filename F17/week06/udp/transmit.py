# UDP demo (Tx to thyself)
#
# Stanley H.I. Lio
# hlio@hawaii.edu
import socket


IP = '127.0.0.1'
PORT = 50005


sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

m = 'beatings will continue until morale improves'

print('sending: ' + m)
sock.sendto(m.encode(),(IP,PORT))
