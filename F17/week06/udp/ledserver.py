# UDP demo
# works with ledcontrol.py
#
# Stanley H.I. Lio
# hlio@hawaii.edu
import RPi.GPIO as GPIO
import time,socket,traceback


pin = 17
IP = ''
PORT = 50006

sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
sock.bind((IP,PORT))

GPIO.setmode(GPIO.BCM)
GPIO.setup(pin,GPIO.OUT)
GPIO.output(pin,GPIO.LOW)


print('Listening...')
while True:
    try:
        data,addr = sock.recvfrom(1024)
        m = data.decode()
        #print(m)

        if 'on' in m:
            print('{} wants it {}'.format(addr[0],m))
            GPIO.output(pin,GPIO.HIGH)
        elif 'off' in m:
            print('{} wants it {}'.format(addr[0],m))
            GPIO.output(pin,GPIO.LOW)
    except KeyboardInterrupt:
        break
    except:
        traceback.print_exc()


print('Cleaning up...')
GPIO.cleanup(pin)
print('Done.')
