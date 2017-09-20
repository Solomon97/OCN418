# File IO (Input/Output) demo - write
#
# Two things to notice:
#   Old content is overwritten every time this is executed
#       Try replacing the 'w' with 'a'
#   The '\n' at the end of both strings (try removing them)
#
# Stanley H.I. Lio
# hlio@hawaii.edu
import time


f = open('haha.csv','w')

f.write('Time is now: {}\n'.format(time.time()))  # "What?" Google "POSIX timestamp".
f.write('single digit millionaires have no effective access to the legal system\n')

f.close()
