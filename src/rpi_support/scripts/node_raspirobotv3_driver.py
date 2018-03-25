#!/usr/bin/env python
'''
This node is a driver for the raspirobot v3 from ROS. For now,
it will also act as the control interface to get inputs from the
motion topic.
'''
import rospy
from std_msgs.msg import String

from raspirobotboard3.python.rrb3 import *

BATTERY_VOLTAGE=9
MOTOR_VOLTAGE=6
LED_ON=1
LED_OFF=0
OC_ON=1
OC_OFF=0

MOTOR_OFF=0
MOTOR_ON=0.5
MOTOR_DIRN_FORWARD=0
MOTOR_DIRN_BACKWARD=1

cmd_to_motors = {
    'F': [MOTOR_ON, MOTOR_DIRN_FORWARD, MOTOR_ON, MOTOR_DIRN_FORWARD],
    'L': [MOTOR_OFF, MOTOR_DIRN_FORWARD, MOTOR_ON, MOTOR_DIRN_FORWARD],
    'R': [MOTOR_ON, MOTOR_DIRN_FORWARD, MOTOR_OFF, MOTOR_DIRN_FORWARD],
    'STOP': [MOTOR_OFF, MOTOR_DIRN_FORWARD, MOTOR_OFF, MOTOR_DIRN_FORWARD],
}


def motion_topic_callback(data):
    rospy.loginfo(rospy.get_caller_id() + "Received %s", data.data)

    if data.data in cmd_to_motors.keys():
        rospy.loginfo(rospy.get_caller_id() + "Moving %s", data.data)
        rr.set_motors(cmd_to_motors[data.data])


def motion_topic_listener():
    rospy.init_node('RaspiRobotV3Driver', anonymous=True)

    rospy.Subscriber("MOTION_TOPIC", String, motion_topic_callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()


def raspirobotv3_init():

    # Switch on the LEDs
    rr.set_led1(LED_ON)
    rr.set_led2(LED_ON)

    # Turn off the open collectors
    rr.set_oc1(OC_OFF)
    rr.set_oc2(OC_ON)

    # Turn off all the motors
    rr.set_motors(MOTOR_OFF, MOTOR_DIRN_FORWARD, MOTOR_OFF, MOTOR_DIRN_FORWARD)

if __name__ == '__main__':
    # Init the raspirobot with the right voltages
    rr = RRB3(BATTERY_VOLTAGE, MOTOR_VOLTAGE)

    raspirobotv3_init()
    motion_topic_listener()
