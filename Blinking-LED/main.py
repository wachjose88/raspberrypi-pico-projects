# Copyright (c) 2024 Josef Wachtler
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

"""
This is a very simple project for the Raspberry Pi Pico. It switches the
integrated LED on and off with an interval of 1 second.
"""

# import required libraries
from machine import Pin
from time import sleep

# Define the LED. This works on a Raspberry Pi Pico W.
# Use the commented version for a Raspberry Pi Pico.
# led = Pin(25, Pin.OUT)
led = Pin('LED', Pin.OUT)

# Define a counter.
c = 0

# Loop forever
while True:
    # Enable the LED. led.high() would also work.
    led.value(1)
    print('on', c)
    c = c + 1

    # Wait a second
    sleep(1)

    # Disable the LED. led.low() would also work.
    led.value(0)
    print('off', c)
    c = c + 1

    # Wait a second
    sleep(1)

