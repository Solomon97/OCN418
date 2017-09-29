# Plot your own "IoT data".
#
# Source:
# https://matplotlib.org/examples/pylab_examples/simple_plot.html
import matplotlib.pyplot as plt
import numpy as np
import requests


d = requests.get('http://192.168.2.200/data.txt')
print(d.text)
exit()

plt.plot(t,s)

plt.xlabel('take the cannoli')
plt.ylabel('leave the gun')
plt.title('why eagles can\'t swim')
plt.grid(True)
plt.savefig('bourgeoisie.png')
plt.show()
