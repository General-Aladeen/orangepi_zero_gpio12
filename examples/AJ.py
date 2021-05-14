from time import sleep
from pyA20.gpio import gpio
from pyA20.gpio import port


gpio.init ()

#LED 1 (TOP RIGHT)
led1R=port.PA0
led1G=port.PA1
led1B=port.PA3
#LED 2 (TOP RIGHT)
led2R = port.PA13
led2G = port.PA10
led2B = port.PA2
#LED 3 (BOTTOM LEFT)
led3R = port.PA11
led3G = port.PA12
led3B = port.PA6
#LED 4 (BOTTOM RIGHT)
led4R = port.PA16
led4G = port.PA15
led4B = port.PA14


#----------Init----------#
gpio.setcfg (led1R, gpio.OUTPUT)
gpio.setcfg (led1G, gpio.OUTPUT)
gpio.setcfg (led1B, gpio.OUTPUT)

gpio.setcfg (led2R, gpio.OUTPUT)
gpio.setcfg (led2G, gpio.OUTPUT)
gpio.setcfg (led2B, gpio.OUTPUT)

gpio.setcfg (led3R, gpio.OUTPUT)
gpio.setcfg (led3G, gpio.OUTPUT)
gpio.setcfg (led3B, gpio.OUTPUT)

gpio.setcfg (led4R, gpio.OUTPUT)
gpio.setcfg (led4G, gpio.OUTPUT)
gpio.setcfg (led4B, gpio.OUTPUT)

i = 0

# set the status of the leds (high / low):
while True:
        gpio.output (led1R, gpio.LOW)
        sleep (0.1)
        gpio.output (led1R, gpio.HIGH)
        sleep (0.1)
        gpio.output (led2R, gpio.LOW)
        sleep (0.1)
        gpio.output (led2R, gpio.HIGH)
        sleep (0.1)
        gpio.output (led4R, gpio.LOW)
        sleep (0.1)
        gpio.output (led4R, gpio.HIGH)
        sleep (0.1)
        gpio.output (led3R, gpio.LOW)
        sleep (0.1)
        gpio.output (led3R, gpio.HIGH)
        sleep (0.1)
        i = i+1
        
        
