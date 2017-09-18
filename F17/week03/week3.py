# LED light bar with "ADC" input
import gpiozero
import time

interval = 0.9
photo = gpiozero.LightSensor(4)

leds = [21, 16, 12, 23]
leds = [gpiozero.LED(led) for led in leds]


while True:
    [led.off() for led in leds]
    v = photo.value
    print(v)
    for i in range(int(v*len(leds))):
        leds[i].on()        
    time.sleep(interval)
