from time import sleep
from pyA20.gpio import gpio
from pyA20.gpio import port


gpio.init ()


led1 = port.PA2
led2 = port.PA3
led3 = port.PA14
led4 = port.PA6

gpio.setcfg (led1, gpio.OUTPUT)
gpio.setcfg (led2, gpio.OUTPUT)
gpio.setcfg (led3, gpio.OUTPUT)
gpio.setcfg (led4, gpio.OUTPUT)
# set the status of the leds (high / low)
while True:
        gpio.output (led1, gpio.LOW)
        gpio.output (led2, gpio.LOW)
        gpio.output (led3, gpio.LOW)
        gpio.output (led4, gpio.LOW)
        sleep (0.1)
        gpio.output (led1, gpio.HIGH)
        gpio.output (led2, gpio.HIGH)
        gpio.output (led3, gpio.HIGH)
        gpio.output (led4, gpio.HIGH)
        sleep (0.1)
        gpio.output (led1, gpio.LOW)
        gpio.output (led2, gpio.LOW)
        gpio.output (led3, gpio.LOW)
        gpio.output (led4, gpio.LOW)
        sleep (0.1)
        gpio.output (led1, gpio.HIGH)
        gpio.output (led2, gpio.HIGH)
        gpio.output (led3, gpio.HIGH)
        gpio.output (led4, gpio.HIGH)
        sleep (1)
        
