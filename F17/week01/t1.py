# my first python script
# this will print 50 random numbers
# load the random number generator

# Python notes:
#   Comments start with a '#'.
#   Indentation matters.
#   Python IS case sensitive.

# See also: Style Guide for Python Code

import random

sampleSize = 50

random.seed(0)

# loop over sampleSize times...
for i in range(sampleSize):
    newValue = random.random()
    print(newValue)   # DON'T FORGET THE (...) for the print() function

