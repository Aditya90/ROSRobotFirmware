#!/usr/bin/env python
import rospy
from std_msgs.msg import String
import Adafruit_BBIO.GPIO as GPIO

#motors = {
#    'front_right': "P9_12",
#    'front_left': "P9_23",
#    'back_right': "P9_25",
#    'back_left': "P9_27"
#}

#cmd_to_motors = {
#    'F': ['front_right', 'front_left', 'back_left', 'back_right'],
#    'L': ['front_right', 'back_right'],
#    'R': ['front_left', 'back_left'],
#    'STOP': []
#}

motors = {
    '1a': "P9_12",
    '2a': "P9_23"
}

cmd_to_motors = {
    'LH': ['2a'],
    'HL': ['1a'],
    'HH': ['1a', '2a'],
    'LL': []
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



def init_motors():

    # Set up the GPIO pins as output
    # GPIO_49   []-----[]    GPIO_60
    #               |
    #               |
    # GPIO_115  []-----[]    GPIO_117

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
