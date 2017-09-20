# Generate some data and write to CSV.
#
# Stanley H.I. Lio
# hlio@hawaii.edu
import numpy as np

t = np.arange(0.0,2.0,0.05)
s = 1 + np.sin(2*np.pi*t)
with open('data.csv','w') as f:
    for p in zip(t,s):
        f.write('{},{}\n'.format(*p))
