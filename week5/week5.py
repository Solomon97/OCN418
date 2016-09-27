#!/usr/bin/env python3
"""
    This program will loop forever, reading the BME, outputting the data,
    and setting the led meter to current temperature value.
    
    This will output data in a comma separated value list as:
    year, month, day, hour, seconds, temperature, pressure, humidity

    as well as send one piece of data across a UDP channel for plotting.
"""

import gpiozero
import time
import sys
import led
import bme280
import ads1115
import datetime
import socket

# Network Variables
udp_host = "192.168.2.236"
udp_port = 9999
udp_user = 0


def main():
    # How often to sample the BME [sec]
    sampling = 0.5

    try:
        # create an AF_INET, STREAM socket (TCP)
        udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    except socket.error as msg:
        print("Failed to create socket: {:s}".format(msg[1]), file=sys.stderr)
        sys.exit()

    # Create an array of LEDs
    meter = led.meter([26, 12, 16, 20, 21], min_value=21, max_value=24)

    # Create the ADS
    sensor = ads1115.ADS1115()

    # Loop forever and display the results
    while True:
        try:
            light = sensor.read_adc(0)
            temperature, pressure, humidity = bme280.readBME280All()
            meter.display(temperature)
            print("{:s},{:2.4f},{:4.4f},{:2.4f},{:d}".format(
                datetime.datetime.utcnow().strftime('%Y,%m,%d,%H,%M,%S.%f'),
                temperature, pressure, humidity, light))

            # Send data to the server
            msg = "{:d},{:f}".format(udp_user, temperature)
            udp.sendto(bytes(msg, 'utf-8'), (udp_host, udp_port))

            # Pause to set our sampling rate
            time.sleep(sampling)

        except KeyboardInterrupt:
            print("Exit!", file=sys.stderr)
            meter.off()
            sys.exit()
        except socket.error as msg:
            print("Server Error: {:s}".format(msg[1]), file=sys.stderr)

if __name__ == "__main__":
    main()








