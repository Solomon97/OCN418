# refactoring: function: why?
import time, random
import RPi.GPIO as GPIO


# definition
button = 21
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
N = len(pins)


def zuko(which):
    for pin in pins:
        GPIO.output(pin, GPIO.LOW)
    GPIO.output(pins[which], GPIO.HIGH)

def azula(level):
    for pin in pins:
        GPIO.output(pin, GPIO.LOW)
    for i in range(level + 1):
        GPIO.output(pins[i], GPIO.HIGH)

def ozai(v):
    s = '''You hear your mom calling you into the kitchen. As you are heading down the stairs you hear a whisper from the closet saying "Don't go down there honey, I heard it too."'''
    r = ['w', 'h', 'i', 's', 'p', 'e', 'r', '.']
    #print(s.count(r[v]) % N)
    azula(s.count(r[v]) % N)

def zokka(v):
    zuko(random.randint(0, N - 1))


while True:
    try:
        if not GPIO.input(button):
            print('light #{}'.format(counter))
            
            counter = (counter + 1) % N

            #zuko(counter)
            azula(counter)
            #ozai(counter)
            #zokka(counter)
            
            while not GPIO.input(button):
                time.sleep(0.1)
    except KeyboardInterrupt:
        print('user interrupted')
        break

GPIO.cleanup()


# At this point you should know the basics of these already:
#   defining and using a variable
#   the "while" and "for" loop
#   defining and calling a function
#   and perhaps exception handling
