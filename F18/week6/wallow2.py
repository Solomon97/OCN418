# Refactoring: list
# It'd be nice to be able to move the LEDs to different pins without changing a lot of code.
import time
import RPi.GPIO as GPIO


# definition
button = 21
counter = 0

# always include but ignore this
GPIO.setmode(GPIO.BCM)

# setup the button input pin
GPIO.setup(button, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# now setup the LED output pins
pins = [17, 27, 22, 5, 6, 13, 19, 26]                       # <- "single source of truth"
for pin in pins:
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.LOW)


while True:
    if not GPIO.input(button):
        print('{} hit'.format(counter))
        
        counter = (counter + 1) % len(pins)

        if 0 == counter:
            for pin in pins:                                # turn off all light
                GPIO.output(pin, GPIO.LOW)
            GPIO.output(17, GPIO.HIGH)                      # <- but what about these?
        if 1 == counter:
            for pin in pins:
                GPIO.output(pin, GPIO.LOW)
            GPIO.output(27, GPIO.HIGH)                      # <-
        if 2 == counter:
            for pin in pins:
                GPIO.output(pin, GPIO.LOW)
            GPIO.output(22, GPIO.HIGH)
        if 3 == counter:
            for pin in pins:
                GPIO.output(pin, GPIO.LOW)
            GPIO.output(5, GPIO.HIGH)
        if 4 == counter:
            for pin in pins:
                GPIO.output(pin, GPIO.LOW)
            GPIO.output(6, GPIO.HIGH)
        if 5 == counter:
            for pin in pins:
                GPIO.output(pin, GPIO.LOW)
            GPIO.output(13, GPIO.HIGH)
        if 6 == counter:
            for pin in pins:
                GPIO.output(pin, GPIO.LOW)
            GPIO.output(19, GPIO.HIGH)
        if 7 == counter:
            for pin in pins:
                GPIO.output(pin, GPIO.LOW)
            GPIO.output(26, GPIO.HIGH)
        
        while not GPIO.input(button):
            time.sleep(0.1)

# Now a pattern emerges: the value of "counter" determines which light to turn on, and this is true for all 8 lights.
