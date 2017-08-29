import numpy as np
import matplotlib.pyplot as plt


# - - - - -
# some important data

x = np.arange(0,1.5*np.pi,0.1)
y = np.sin(x)


# - - - - -
# the beef

fig = plt.figure()

ax1 = fig.add_subplot(2,1,1)
ax1.plot(x,y)
ax1.set_xlabel('is people')
ax1.set_ylabel('green')
ax1.set_title('soylent')

ax2 = fig.add_subplot(2,1,2)
ax2.plot(x,-y)
ax2.set_xlabel('in laws')
ax2.set_ylabel("neighbor's dog")
ax2.set_title('step on a LEGO')

plt.tight_layout()
plt.show()
