# refactoring: function
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


# this defines a function named "zuko" which expects a single argument
def zuko(which):
    for pin in pins:
        GPIO.output(pin, GPIO.LOW)
    GPIO.output(pins[which], GPIO.HIGH)


while True:
    try:
        if not GPIO.input(button):
            print('light #{}'.format(counter))
            
            counter = (counter + 1) % N

            zuko(counter)
            
            while not GPIO.input(button):
                time.sleep(0.1)
    except KeyboardInterrupt:
        print('user interrupted')
        break

GPIO.cleanup()


# ... but why bother?
