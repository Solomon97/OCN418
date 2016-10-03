#!/usr/bin/env python3
import gpiozero,time,sys,bme280,ads1115
from datetime import datetime


sample_period = 1
sensor = ads1115.ADS1115()

while True:
    try:
        light = sensor.read_adc(0)
        temperature,pressure,humidity = bme280.readBME280All()
        print("{:s},{:2.4f},{:4.4f},{:2.4f},{:d}".format(
            datetime.datetime.utcnow().strftime('%Y,%m,%d,%H,%M,%S.%f'),
            temperature, pressure, humidity, light))

        time.sleep(sample_period)

    except KeyboardInterrupt:
        print("Exit!")
        sys.exit()
