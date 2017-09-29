# Log everything received to txt
#
# Stanley H.I. Lio
# hlio@hawaii.edu
import socket,traceback


IP = ''
PORT = 50007

sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
sock.bind((IP,PORT))

print('Listening...')
with open('/var/www/html/data.txt','a',1) as f:
    while True:
        try:
            data,addr = sock.recvfrom(1024)
            print(data.decode().strip())
            f.write(data.decode().strip() + '\n')
        except KeyboardInterrupt:
            break
        except:
            traceback.print_exc()
