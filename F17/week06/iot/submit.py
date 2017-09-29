# Submit temperature data to the OCN418 IoT server
#
# Stanley H.I. Lio
# hlio@hawaii.edu
import socket,sys,time,traceback
sys.path.append('../../week04')
from bmp280_Py3driver import BMP280


IP = '192.168.2.200'
PORT = 50007
myid = socket.gethostname()
print('I\'m ' + myid)

sensor = BMP280()
sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

while True:
    try:
        r = sensor.read()
        print(r)

        m = '{},{},{}\n'.format(myid,time.time(),r['t'])
        print('sending: ' + m.strip())
        sock.sendto(m.encode(),(IP,PORT))
        
        time.sleep(60)
    except KeyboardInterrupt:
        break
    except:
        traceback.print_exc()

