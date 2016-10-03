import numpy as np
import matplotlib.pyplot as plt


# - - - - -
# read text file
D = []
with open('week6data.txt') as f:
    for line in f:
        line = line.strip().split(',')
        D.append([line[0],float(line[1]),float(line[2])])

#D = zip(*D)
#print(D)


# - - - - -
# choose your variable
x = D[1]
y = D[2]


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
