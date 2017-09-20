# UDP demo (broadcast)
#
# Stanley H.I. Lio
# hlio@hawaii.edu
from socket import *
from datetime import datetime


IP = '255.255.255.255'
PORT = 5005

sock = socket(AF_INET,SOCK_DGRAM)
sock.setsockopt(SOL_SOCKET,SO_BROADCAST,1)


name = 'Steven Universe'
pi = gethostname()
t = datetime.now()
m = 'This is {} broadcasting from {}. Time is now: {}'.format(name,pi,t)

print('broadcasting: ' + m)
sock.sendto(m.encode(),(IP,PORT))
