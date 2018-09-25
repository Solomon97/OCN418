# Data structure: list: indexing
import time
import RPi.GPIO as GPIO


# definition
button = 21
N = 8
counter = 0

# ignore this
GPIO.setmode(GPIO.BCM)

# setup the button input pin
GPIO.setup(button, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# now setup the LED output pins
pins = [17, 27, 22, 5, 6, 13, 19, 26]
for pin in pins:
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.LOW)
GPIO.output(pins[0], GPIO.HIGH)


while True:
    try:                                                    # <- exception handling
        if not GPIO.input(button):
            print('light #{}'.format(counter))
            
            counter = (counter + 1) % N

            for pin in pins:
                GPIO.output(pin, GPIO.LOW)
            GPIO.output(pins[counter], GPIO.HIGH)           # <- indexing: the "counter" position in the list "pins"
            
            while not GPIO.input(button):
                time.sleep(0.1)
    except KeyboardInterrupt:
        print('user interrupted')
        break

GPIO.cleanup()
