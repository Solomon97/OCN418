import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime


# - - - - -
# read text file
D = []
with open('/home/pi/python/whatevertextyouhave.csv') as f:
    for line in f:
        line = line.strip().split(',')
        line = [float(tmp) for tmp in line]
        #dt = datetime(int(line[0]),int(line[1]),int(line[2]),int(line[3]),int(line[4]),int(line[5]))
        D.append(line)

D = zip(*D)


# - - - - -
# choose your variable
x = range(0,len(D[1]))
y = D[6]


# - - - - -
# da beef
fig = plt.figure()

ax1 = fig.add_subplot(1,1,1)
ax1.plot(x,y)
ax1.set_xlabel('is people')
ax1.set_ylabel('green')
ax1.set_title('soylent')


plt.tight_layout()
plt.show()
