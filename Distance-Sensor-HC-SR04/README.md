# Distance Sensor HC-SR04

This is a library and its usage for the distance sensor HC-SR04. It measures
the distance by using ultrasonic sounds.

The HC-SR04 sends out an ultrasonic sound if the trigger is set.
By measuring the time until the sound is bounced back by a wall and
recognized by echo.

This sensor has four pins. The first one is VCC and it should be
wired to physical pin number 36 called "3V3(OUT)". The last pin
is labeled GND and should be connected to one of the GND pins.
The trigger pin should be labeled to a GPIO output pin and the
echo pin to a GPIO input pin.

![wirering diagramm](/Distance-Sensor-HC-SR04/distance.png)

At first it activates the trigger and then it waits for the echo.
After that the time difference is calculated and multiplied by the speed of
sound and divided by two, because the measuring sound travels to
the wall and back.
