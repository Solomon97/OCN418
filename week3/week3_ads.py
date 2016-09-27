#!/usr/bin/env python3
"""
    This program will loop forever, reading the Sensors, outputting the data,
    and setting the led meter to one of the sensor values.
"""

import time
import sys
import led
import ads1115

# Our program to run


def main():
    # How often to sample the ADS [sec]
    sampling = 0.5

    # Create an array of LEDs
    meter = led.meter([26, 12, 16, 20, 21], 13000, 15000)

    # Create the ADS
    sensor = ads1115.ADS1115()

    # Loop forever and display the results
    try:
        while True:
            light = sensor.read_adc(0)
            meter.display(light)

    except KeyboardInterrupt:
        print("Exit!", file=sys.stderr)
        meter.off()

if __name__ == "__main__":
    main()

