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
integrated LED on and off if a physical button is pressed. The LED remains on
while the button is held down.
"""

# import required libraries
from machine import Pin
from time import sleep
# Define the LED. This works on a Raspberry Pi Pico W.
# Use the commented version for a Raspberry Pi Pico.
# led = Pin(25, Pin.OUT)
led = Pin('LED', Pin.OUT)

# Define the button input pin. Use a button which closes the circuit if it is
# pressed down. Wire the button from the pin "3V3(OUT)" which is physical pin
# number 36 to the pin "GP14" which is physical pin number 19.
button = Pin(14, Pin.IN, Pin.PULL_DOWN)

# Loop forever
while True:
    # Get the state of the button. 1 means the button is held down.
    state = button.value()
    print(state)

    # If the button is held down enable the LED, else disable it.
    if state == 1:
        led.high()
    else:
        led.low()

    # Sleep for 0.1 seconds
    sleep(0.1)
