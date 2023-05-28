from machine import Pin, PWM

piezo = PWM(Pin(28))
button = Pin(27, Pin.IN, Pin.PULL_DOWN)