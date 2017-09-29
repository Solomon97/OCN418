# submit random data
#
# Stanley H.I. Lio
# hlio@hawaii.edu
import socket,time,random


IP = '192.168.2.200'
PORT = 50007
myid = socket.gethostname()
print('I\'m ' + myid)

sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

m = '{},{},{}\n'.format(myid,time.time(),random.random())

print('sending: ' + m.strip())
sock.sendto(m.encode(),(IP,PORT))
