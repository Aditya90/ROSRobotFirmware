#!/bin/bash

# First we need to run roscore
#gnome-terminal -e "roscore" --title=roscore

# Update the workspace
source ./devel/setup.bash
catkin_make
catkin_make install

source ./devel/setup.bash
