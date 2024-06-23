from hal import hal_led as led
from threading import Thread
from time import sleep

def led_thread():
    global delay
    delay = 0

    while True:
        if delay != 0:
            led.set_output(20, 1)
            sleep(delay)
            led.set_output(20, 0)
            sleep(delay)
        else:
            sleep(1)

def led_off():
    global delay
    delay = 0

def led_control_init():
    global delay
    led.init()
    t1 = Thread(target=led_thread)
    t1.start()
    delay = 1
