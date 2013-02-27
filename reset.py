#!/usr/bin/python
import RPIO
import os
import time

int_pin = 10

def do_something(gpio_id, value):
    print "reboot"
    time.sleep(0.5)
    os.system("shutdown -r +1")

RPIO.add_interrupt_callback(int_pin, do_something, pull_up_down=RPIO.PUD_UP, edge='falling')
RPIO.wait_for_interrupts()
