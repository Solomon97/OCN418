#!/usr/bin/env python3
"""
    This program will loop forever, reading the BME, outputting the data,
    and setting the led meter to current temperature value.
    
    This will output data in a comma separated value list as:
    year, month, day, hour, seconds, temperature, pressure, humidity
"""

import gpiozero
import time
import sys
import led
import bme280
from datetime import datetime

# Our program to run


def main():
    # How often to sample the BME [sec]
    sampling = 0.5

    # Create an array of LEDs
    meter = led.meter([26, 12, 16, 20, 21], min_value=21, max_value=24)

    # Loop forever and display the results
    try:
        while True:
            temperature, pressure, humidity = bme280.readBME280All()
            meter.display(temperature)
            print("{:s},{:2.4f},{:4.4f},{:2.4f}".format(
                datetime.utcnow().strftime('%Y,%m,%d,%H,%M,%S.%f'),
                temperature, pressure, humidity))
            time.sleep(sampling)

    except KeyboardInterrupt:
        print("Exit!", file=sys.stderr)
        meter.off()

if __name__ == "__main__":
    main()








