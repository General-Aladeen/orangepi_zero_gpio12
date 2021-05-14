from time import sleep
from pyA20.gpio import gpio
from pyA20.gpio import port


gpio.init ()


led = port.PA13

gpio.setcfg (led, gpio.OUTPUT)
# set the status of the leds (high / low)
while True:
        gpio.output (led, gpio.HIGH)
        sleep (0.5)
        gpio.output (led, gpio.LOW)
        sleep (1)
