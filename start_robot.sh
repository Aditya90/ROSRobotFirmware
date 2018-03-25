#!/bin/bash

echo "Opening a screen for the roscore"
screen -A -m -d -S "roscore" "run_roscore.sh"
echo "Opening a screen for the ros keyboard"
screen -A -m -d -S "keyboard" "run_keyboard.sh"
echo "Opening a screen for the ros gpio"
screen -A -m -d -S "gpio" "run_gpio.sh"


