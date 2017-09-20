# File IO demo - read
#
# Stanley H.I. Lio
# hlio@hawaii.edu
import time


f = open('haha.csv','r')
# Of course, you can do this too:
#f = open('read.py','r')
for line in f:
    print(line.strip())
f.close()


print('\n\n- - - - - Don\'t mind me I\'m just a separator - - - - -\n\n')


# (optional) More concisely:
for line in open('haha.csv','r'):
    print(line.strip())
