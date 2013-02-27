import RPIO
import time
import os

#gpio 4 is pin 7
#gpio 3 is pin 5
led_pin = 11
int_pin = 9
def do_something(gpio_id, value):
    print "starting vid"
    RPIO.output(led_pin, True)
    time.sleep(1)
    RPIO.output(led_pin, False)

    #("New value for GPIO %s: %s" % (gpio_id, value))
    #os.system("mplayer -vo fbdev2:/dev/fb0 -framedrop test.avi")
    print "finished"


RPIO.setup(led_pin, RPIO.OUT, initial=RPIO.LOW)
RPIO.add_interrupt_callback(int_pin, do_something, edge='rising')
RPIO.wait_for_interrupts()
