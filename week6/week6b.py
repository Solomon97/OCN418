#!/usr/bin/env python3
import gpiozero,time,sys
sys.path.append('../week3')
import bme280,ads1115
from datetime import datetime
import calendar


sample_period = 1
sensor = ads1115.ADS1115()

with open('week6data.txt','a') as f:
    while True:
        try:
            dt = datetime.utcnow()
            ts = calendar.timegm(dt.timetuple())
            adc = sensor.read_adc(0)/32767.0
            temperature,pressure,humidity = bme280.readBME280All()

            line = "{},{},{:2.2f},{:4.2f},{:2.2f},{:.6f}".\
                  format(dt.isoformat(),ts,temperature,pressure,humidity,adc)
            print(line)
            f.write(line + '\n')

            time.sleep(sample_period)

        except KeyboardInterrupt:
            print("Exit!")
            sys.exit()
