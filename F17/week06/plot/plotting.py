# Plot two cycles of a sine wave.
#
# Source:
# https://matplotlib.org/examples/pylab_examples/simple_plot.html
import matplotlib.pyplot as plt
import numpy as np


t = np.arange(0.0,2.0,0.01)
s = 1 + np.sin(2*np.pi*t)

plt.plot(t,s)

plt.xlabel('take the cannoli')
plt.ylabel('leave the gun')
plt.title('why eagles can\'t swim')
plt.grid(True)
plt.savefig('bourgeoisie.png')
plt.show()
