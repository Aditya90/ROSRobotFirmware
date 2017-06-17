#!/usr/bin/env python
import rospy
from std_msgs.msg import String
import Adafruit_BBIO.GPIO as GPIO


def motion_topic_callback(data):
    rospy.loginfo(rospy.get_caller_id() + "Moving %s", data.data)


def init_motors():
    # Set up the GPIO pins as output
    # GPIO_49   []-----[]    GPIO_60
    #               |
    #               |
    # GPIO_117  []-----[]    GPIO_115
    motors = {
        'front_right': "P9_12",
        'front_left': "P9_23",
        'back_right': "P9_25",
        'back_left': "P9_27"
    }

    # Setup all motor pins as output
    for motorPins in motors.values():
        GPIO.setup(motorPins, GPIO.OUT)


def motion_topic_listener():
    init_motors()
    rospy.init_node('GpioOutput', anonymous=True)

    rospy.Subscriber("MOTION_TOPIC", String, motion_topic_callback)

    # spin() simply keeps python from exiting until this node is stopped

    rospy.spin()

if __name__ == '__main__':
    motion_topic_listener()
