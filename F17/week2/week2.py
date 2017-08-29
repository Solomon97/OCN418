import RPi.GPIO as GPIO
import time


GPIO.setmode(GPIO.BOARD)
pin_to_circuit = 7


def rc_time(pin_to_circuit):
    GPIO.setup(pin_to_circuit,GPIO.OUT)
    GPIO.output(pin_to_circuit,GPIO.LOW)
    time.sleep(0.1)

    GPIO.setup(pin_to_circuit,GPIO.IN)
    
    count = 0
    while (GPIO.input(pin_to_circuit) == GPIO.LOW):
        count = count + 1
    return count

while True:
    print(rc_time(pin_to_circuit))

GPIO.cleanup()
