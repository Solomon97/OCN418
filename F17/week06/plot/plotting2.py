# Plot your own "IoT data".
#
# In terminal, do this first: "pip3 install requests"
#
# Stanley H.I. Lio
# hlio@hawaii.edu
import matplotlib.pyplot as plt
import requests,socket,traceback


# FETCHING
d = requests.get('http://192.168.2.200/data.txt')
#print(d.text)


# PARSING
myid = socket.gethostname()
x,y = [],[]
for line in d.text.split('\n'):
    try:
        line = line.strip().split(',')
        if myid == line[0]:
            print(line)
            x.append(float(line[1]))
            y.append(float(line[2]))
    except:
        traceback.print_exc()


# PLOTTING
plt.plot(x,y)
plt.xlabel('Seconds since 1970, hopefully')
plt.ylabel('Probably temperature')
plt.title('Likely to be Temperature Data')
plt.grid(True)
plt.savefig('birdwatcher.png')
plt.show()
