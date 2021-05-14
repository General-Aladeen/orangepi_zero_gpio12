from time import sleep
from pyA20.gpio import gpio
from pyA20.gpio import port

Start #gpio functions.
gpio.init ()

Set #gpio.
led = port.PA6
gpio.setcfg (led, gpio.OUTPUT)

# set the status of the leds (high / low)
while True:
        gpio.output (led, gpio.HIGH)
        sleep (1)
        gpio.output (led, gpio.LOW)
        sleep (1)
