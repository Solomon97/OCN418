import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import sys
sys.path.append('../week3')
import ads1115

fig, ax = plt.subplots()
line, = ax.plot(np.random.rand(10))
ax.set_ylim(0, 1)


sensor = ads1115.ADS1115()

D = []
def update(data):
    print data
    D.append(data)
    while len(D) > 100:
        D.pop(0)
    line.set_xdata(range(0,len(D)))
    line.set_ydata(D)
    return line,


def data_gen():
    #while True:
        #yield np.random.rand(10)
    yield sensor.read_adc(0)

ani = animation.FuncAnimation(fig, update, data_gen, interval=100)
plt.show()
