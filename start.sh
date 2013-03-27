#!/bin/bash
cd /home/pi/skiptv
#clear screen!
dd if=/dev/zero of=/dev/fb0
setterm -cursor off > /dev/tty1
date >> log.text
./player.py >> log.text 2>&1 &
