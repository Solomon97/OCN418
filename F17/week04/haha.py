import sys,time
sys.path.append('/home/pi/Desktop/OCN418/F17/week04')
from lcd20x4 import LCD


lcd = LCD(bus=1,address=0x3f)

line = 'should we gather for whisky and cigar tonight?'

#lcd.write_lines(['cast','into','the bowel','of the earth'])

i = 0

while True:
    lcd.write_lines([line[i:i+20],'','',''])
    time.sleep(1)
    i = i + 1
    i = i % 20
