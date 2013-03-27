#!/usr/bin/python
import RPIO
import time
import os

#see http://elinux.org/RPi_Low-level_peripherals#GPIO_hardware_hacking
led_pin = 14
int_pin = 15

def play_vid(gpio_id, value):
    print "starting vid"
    RPIO.output(led_pin, True)

    #("New value for GPIO %s: %s" % (gpio_id, value))
    os.system("mplayer -vo fbdev2:/dev/fb0 -framedrop /home/pi/skiptv/testshort.avi")
    RPIO.output(led_pin, False)
    print "finished"


RPIO.setup(led_pin, RPIO.OUT, initial=RPIO.LOW)
RPIO.add_interrupt_callback(int_pin, play_vid, edge='rising')
RPIO.wait_for_interrupts()
