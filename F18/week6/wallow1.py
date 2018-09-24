# Data structure and function
# Continue from week 5...
# We had 3 light. Then we had 5. What if we have more?
import time
import RPi.GPIO as GPIO


button = 21
N = 8
counter = 0

GPIO.setmode(GPIO.BCM)
GPIO.setup(button, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(27, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)
GPIO.setup(5, GPIO.OUT)
GPIO.setup(6, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)
GPIO.setup(19, GPIO.OUT)
GPIO.setup(26, GPIO.OUT)


while True:
    if not GPIO.input(button):
        print('{} hit'.format(counter))
        
        counter = (counter + 1) % N

        if 0 == counter:
            GPIO.output(17, GPIO.HIGH)
            GPIO.output(27, GPIO.LOW)
            GPIO.output(22, GPIO.LOW)
            GPIO.output(5, GPIO.LOW)
            GPIO.output(6, GPIO.LOW)
            GPIO.output(13, GPIO.LOW)
            GPIO.output(19, GPIO.LOW)
            GPIO.output(26, GPIO.LOW)
        if 1 == counter:
            GPIO.output(17, GPIO.LOW)
            GPIO.output(27, GPIO.HIGH)
            GPIO.output(22, GPIO.LOW)
            GPIO.output(5, GPIO.LOW)
            GPIO.output(6, GPIO.LOW)
            GPIO.output(13, GPIO.LOW)
            GPIO.output(19, GPIO.LOW)
            GPIO.output(26, GPIO.LOW)
        if 2 == counter:
            GPIO.output(17, GPIO.LOW)
            GPIO.output(27, GPIO.LOW)
            GPIO.output(22, GPIO.HIGH)
            GPIO.output(5, GPIO.LOW)
            GPIO.output(6, GPIO.LOW)
            GPIO.output(13, GPIO.LOW)
            GPIO.output(19, GPIO.LOW)
            GPIO.output(26, GPIO.LOW)
        if 3 == counter:
            GPIO.output(17, GPIO.LOW)
            GPIO.output(27, GPIO.LOW)
            GPIO.output(22, GPIO.LOW)
            GPIO.output(5, GPIO.HIGH)
            GPIO.output(6, GPIO.LOW)
            GPIO.output(13, GPIO.LOW)
            GPIO.output(19, GPIO.LOW)
            GPIO.output(26, GPIO.LOW)
        if 4 == counter:
            GPIO.output(17, GPIO.LOW)
            GPIO.output(27, GPIO.LOW)
            GPIO.output(22, GPIO.LOW)
            GPIO.output(5, GPIO.LOW)
            GPIO.output(6, GPIO.HIGH)
            GPIO.output(13, GPIO.LOW)
            GPIO.output(19, GPIO.LOW)
            GPIO.output(26, GPIO.LOW)
        if 5 == counter:
            GPIO.output(17, GPIO.LOW)
            GPIO.output(27, GPIO.LOW)
            GPIO.output(22, GPIO.LOW)
            GPIO.output(5, GPIO.LOW)
            GPIO.output(6, GPIO.LOW)
            GPIO.output(13, GPIO.HIGH)
            GPIO.output(19, GPIO.LOW)
            GPIO.output(26, GPIO.LOW)
        if 6 == counter:
            GPIO.output(17, GPIO.LOW)
            GPIO.output(27, GPIO.LOW)
            GPIO.output(22, GPIO.LOW)
            GPIO.output(5, GPIO.LOW)
            GPIO.output(6, GPIO.LOW)
            GPIO.output(13, GPIO.LOW)
            GPIO.output(19, GPIO.HIGH)
            GPIO.output(26, GPIO.LOW)
        if 7 == counter:
            GPIO.output(17, GPIO.LOW)
            GPIO.output(27, GPIO.LOW)
            GPIO.output(22, GPIO.LOW)
            GPIO.output(5, GPIO.LOW)
            GPIO.output(6, GPIO.LOW)
            GPIO.output(13, GPIO.LOW)
            GPIO.output(19, GPIO.LOW)
            GPIO.output(26, GPIO.HIGH)
        
        while not GPIO.input(button):
            time.sleep(0.1)


# That's a lot of typing and not a lot of programming.
