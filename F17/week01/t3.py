# Demo 3: Raspberry Pi Input Output control (RPi GPIO)
import gpiozero,time

pin = 26
interval = 0.1

led = gpiozero.LED(pin)

# Hit "Ctrl + C" to kill a running Python script

# on() brings the GPIO "HIGH".

while True:
    print("ON")
    led.on()
    time.sleep(interval)

    print("OFF")
    led.off()
    time.sleep(9*interval)
    
