from time import sleep
from pyA20.gpio import gpio
from pyA20.gpio import port


gpio.init ()


led = port.PA3
led1 = port.PA2
gpio.setcfg (led, gpio.OUTPUT)
gpio.setcfg (led1, gpio.OUTPUT)
# set the status of the leds (high / low)
while True:
        gpio.output (led, gpio.HIGH)
        gpio.output (led1, gpio.HIGH)
        sleep (0.5)
        gpio.output (led, gpio.LOW)
        gpio.output (led1, gpio.LOW)
        sleep (1)
