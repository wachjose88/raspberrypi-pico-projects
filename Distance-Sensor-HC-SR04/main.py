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
This is a library and its usage for the distance sensor HC-SR04. It measures
the distance by using ultrasonic sounds.
"""

# import required libraries
from machine import Pin
from time import sleep, sleep_us, ticks_us

class HCSR04():
    """
    This class represents the distance sensor HC-SR04. It can be used
    for many different projects and multiple times per one board.

    The HC-SR04 sends out an ultrasonic sound if the trigger is set.
    By measuring the time until the sound is bounced back by a wall and
    recognized by echo.

    This sensor has four pins. The first one is VCC and it should be
    wired to physical pin number 36 called "3V3(OUT)". The last pin
    is labeled GND and should be connected to one of the GND pins.
    The trigger pin should be labeled to a GPIO output pin and the
    echo pin to a GPIO input pin.
    """

    def __init__(self, trigger, echo, debug=False):
        """
        Constructor. It inits the pins.

        Positional arguments:
            - trigger -- number of the GPIO output pin to
                         trigger the measurement
            - echo -- number of the GPIO input pin to receive
                      bounced back signal

        Keyword arguments:
            - debug -- True if debug messages should be printed
        """
        self.trigger = Pin(trigger, Pin.OUT)
        self.echo = Pin(echo, Pin.IN)
        self.debug = debug

    def distance(self):
        """
        This method calculates the measured distance. At first it
        activates the trigger and then it waits for the echo. After that
        the time difference is calculated and multiplied by the speed of
        sound and divided by two, because the measuring sound travels to
        the wall and back.
        The measured distance is returned as a float in cm.
        """
        self.trigger.low()
        sleep_us(2)
        self.trigger.high()
        sleep_us(5)
        self.trigger.low()

        while self.echo.value() == 0:
           signaloff = ticks_us()

        while self.echo.value() == 1:
           signalon = ticks_us()

        timepassed = signalon - signaloff

        # 34320 cm/s at 20 °C
        distance = timepassed * 0.03432 / 2

        if self.debug:
            print('     Off:', signaloff)
            print('      On:', signalon)
            print('    Time:', timepassed)
            print('Distance:', str("%.2f" % distance), 'cm')
            print('-' * 42)
        return distance

if __name__ == "__main__":
    # Use the class of the sensor. In this case the trigger pin is
    # GP16 and the echo pin is GP17.
    d = HCSR04(16, 17, True)

    # The distance is measured every 3 seconds forever.
    while True:
        d.distance()
        sleep(3)
