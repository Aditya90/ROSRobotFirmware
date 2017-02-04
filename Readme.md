# README

[License](LICENSE)

## Introduction
This project is aimed at creating a robot based on the Beagle Bone Black and a Zeroborg board using the ROS
architecture. The motivations behind this are :

1. Create a software package which is modular so that individual components (like motor drivers) can be easily
replaced.
2. Learn ROS - because I want to
3. Get more experience with Python and Linux programming

## Getting started

1. Install Ubuntu 14.04 and ROS Indigo on BBB  from instructions on http://charette.no-ip.com:81/programming/2015-06-07_BeagleBoneBlack/
and https://fleshandmachines.wordpress.com/2015/08/25/beaglebone-black-ubuntu-14-04-ros-indigo-install/.
2. Follow the instructions on the [setup shell script](run_package.sh) on how to get the program started.

## References

1. Installing Ubuntu on the BBB - http://charette.no-ip.com:81/programming/2015-06-07_BeagleBoneBlack/
2. Installing ROS on BBB (the ubuntu img file links do not work here, but ROS installation is straightforward)
- https://fleshandmachines.wordpress.com/2015/08/25/beaglebone-black-ubuntu-14-04-ros-indigo-install/.
3. Zeroborg reference - https://www.piborg.org/zeroborg

## Designs

### Basic Motion Control
![ROS Motion Control Structure](doc/basic-motion-design.jpg)