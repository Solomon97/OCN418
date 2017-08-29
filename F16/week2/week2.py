import gpiozero
import time

# Define the functions we use
def initialize(leds):
    """
    Given a list of leds, blink each one in sequence
    """ 
    leds_off(leds)
    for led in leds:
        led.on()
        time.sleep(interval)
        led.off()

def leds_off(leds):
    """
    Given a list of leds, turn each of them off
    """
    for led in leds:
        led.off()

def test_photoresistor(photo):
    """
    Loop infinitely printing out the value of the photoresistor
    so we can understand the range
    """
    while True:
        print(photo.value)
        time.sleep(interval)

def monitor_light(leds=None, photo=None, maxr=1, minr=0):
    """
    Loop infinitely and monitor the light level. Light up the number
    of LEDs depending on the value within the range specified
    """
    # Compute the ratio that relates the value to number of LEDS
    ratio = len(leds) / (maxr - minr)

    while True:
        nleds = int(ratio * (photo.value - minr))
        leds_off(leds)
        for i in range(nleds):
            leds[i].on()
        time.sleep(interval)
    
# Our program to run

# How fast to blink the LED [seconds]
interval = 0.15

# Create an array of LEDs
led_pins = [26, 12, 16, 20, 21]
leds = []
for pin in led_pins:
    leds.append(gpiozero.LED(pin))

# Create the photoresistor
light = gpiozero.LightSensor(13)
initialize(leds)
# test_photoresistor(light)
monitor_light(leds=leds, photo=light, maxr=0.95, minr=0.85)

