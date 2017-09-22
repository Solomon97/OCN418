# Send BMP180 readings periodically through UDP.
#
# Stanley H.I. Lio
# hlio@hawaii.edu
import socket,sys,time
sys.path.append('../../week04')
from bmp280_Py3driver import BMP280


# your ID can be an integer in [1,20]
myid = 1

IP = '192.168.2.200'
PORT = 9999


sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
sensor = BMP280()

while True:
    r = sensor.read()
    m = '{},{}'.format(myid,r['t'])
    print(m)
    sock.sendto(bytearray(m,encoding='ascii'),(IP,PORT))
    time.sleep(1)
