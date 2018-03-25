#!/usr/bin/env python
import rospy
from std_msgs.msg import String
import Adafruit_BBIO.GPIO as GPIO


motors = {
    'left_pos': "P9_12",
    'left_neg': "P9_23",
    'right_pos': "P9_25",
    'right_neg': "P9_27"
}

cmd_to_motors = {
    'F': ['left_pos', 'right_pos'],
    'L': ['right_pos'],
    'R': ['left_pos'],
    'B': ['left_neg', 'right_neg']
}


def motion_topic_callback(data):
    rospy.loginfo(rospy.get_caller_id() + "Moving %s", data.data)

    if data.data in cmd_to_motors.keys():
        for motorToOff in list(set(motors.keys()) - set(cmd_to_motors[data.data])):
            rospy.loginfo("Switching OFF %s", motorToOff)
            GPIO.output(motors[motorToOff], GPIO.LOW)

        for motorToOn in cmd_to_motors[data.data]:
            rospy.loginfo("Switching ON %s", motorToOn)
            GPIO.output(motors[motorToOn], GPIO.HIGH)
    else:
        for motorToOff in motors.keys():
            rospy.loginfo("Switching OFF %s", motorToOff)
            GPIO.output(motors[motorToOff], GPIO.LOW)


def init_motors():

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
