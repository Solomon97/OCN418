import gpiozero
import time

# How fast to blink the LED [seconds]
interval = 0.75

# Create an LED
led = gpiozero.LED(26)

# Turn it on and off and wait for the interval each time
while True:
    led.on()
    time.sleep(interval)
    led.off()
    time.sleep(interval)
