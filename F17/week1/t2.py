#!/usr/bin/python3
# (it's a linux convention. look up #!/bin/bash)
# Demo 2, the "time" module
import random,time

sampleSize = 5

random.seed(0)

for i in range(sampleSize):
    newValue = random.random()
    print(i,newValue)
    time.sleep(0.5)
    
#quit()   #??

