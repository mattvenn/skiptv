import RPIO

#gpio 4 is pin 7
def do_something(gpio_id, value):
    print("New value for GPIO %s: %s" % (gpio_id, value))

RPIO.add_interrupt_callback(4, do_something, edge='rising')
RPIO.wait_for_interrupts()
