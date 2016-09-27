#!/usr/bin/env python3
"""
    This module manages led arrays on the Raspberry Pi
"""

import gpiozero
import time


class array:
    """
    This object will manage a list of GPIO pins that are connected
    to LEDs. It will cycle the lights on initialization, and allow
    you to enable or disable a light by index (rather than pin).

    led.array(pins)

    pins is a list of GPIO pins that are connected to LEDs. The order
    of the array is the order to use the lights.
    """

    def __init__(self, pins=None):
        self.leds = []
        for pin in pins:
            led = gpiozero.LED(pin)
            self.leds.append(led)
            led.off()
            led.on()
            time.sleep(0.2)
            led.off()
        self.nleds = len(self.leds)

    def on(self, idx=None):
        """
        Turn the given LED index on. If not specified, all are turned on
        """
        if idx is not None:
            self.leds[idx].on()
        else:
            for led in self.leds:
                led.on()

    def off(self, idx=None):
        """
        Turn the given LED index off. If not specified, all are turned off
        """
        if idx is not None:
            self.leds[idx].off()
        else:
            for led in self.leds:
                led.off()

    def __len__(self):
        return len(self.leds)


class meter(array):
    """
    This class will manage an led_array, displaying numeric values on the
    LEDs. By default, if the values exceed the minimum or maximum bounds, it
    will adjust the bounds as the data are used.

    led.meter(pins, [min_value], [max_value], [auto_adjust])

    The pins argument is required and defines the pins to use. The min_
    and max_value define the bounds and are optional. The auto_adjust is
    a boolean defining whether the bounds are adaptive.
    """

    def __init__(self, pins=None, min_value=0, max_value=1, auto_adjust=True):
        self.min = min_value
        self.max = max_value
        self.adjust = auto_adjust
        super().__init__(pins)

    def display(self, value=0):
        """
        Given a reading, light up the appropriate number of LEDs
        """
        # If we are auto-adjusting, respond to the value
        if self.adjust:
            self.min = min(self.min, value)
            self.max = max(self.max, value)

        # Compute the ratio that relates the value to number of LEDS
        ratio = self.nleds / (self.max - self.min)

        num_leds = min(int(ratio * (value - self.min)), self.nleds)
        self.off()
        for i in range(num_leds):
            self.on(i)
