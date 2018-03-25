#!/usr/bin/env python
'''
This node is a driver for the raspirobot v3 from ROS. For now,
it will also act as the control interface to get inputs from the
motion topic.
'''
import rospy
from std_msgs.msg import String

from rrb3 import *

# The robot operates on six 1.5 V batteries - 9V
BATTERY_VOLTAGE = 9

# The motors are rated at 6V
MOTOR_VOLTAGE = 6


class RaspiRobot():
    '''
    A wrapper class for the RRB3 object defined by the raspirobot library.
    '''

    LED_ON = 1
    LED_OFF = 0
    OC_ON = 1
    OC_OFF = 0

    MOTOR_OFF = 0
    MOTOR_ON = 0.5 # Use 50% duty cycle as default for now
    MOTOR_DIRN_FORWARD = 0
    MOTOR_DIRN_BACKWARD = 1

    DIRN_TO_MOTOR_INPUTS = {
        'F': [MOTOR_ON, MOTOR_DIRN_FORWARD, MOTOR_ON, MOTOR_DIRN_FORWARD],
        'L': [MOTOR_OFF, MOTOR_DIRN_FORWARD, MOTOR_ON, MOTOR_DIRN_FORWARD],
        'R': [MOTOR_ON, MOTOR_DIRN_FORWARD, MOTOR_OFF, MOTOR_DIRN_FORWARD],
        'B': [MOTOR_ON, MOTOR_DIRN_BACKWARD, MOTOR_ON, MOTOR_DIRN_BACKWARD],
        'STOP': [MOTOR_OFF, MOTOR_DIRN_FORWARD, MOTOR_OFF, MOTOR_DIRN_FORWARD],
    }

    def __init__(self, battery_voltage, motor_voltage):
        '''
        Initialize an object to control the robot
        :param battery_voltage: Voltage of the input power supply to the Board
        :param motor_voltage: Voltage at which the motor operates
        '''

        # Create an RRB3 object to control the robot and initialize
        # it with the passed in values.
        self.rr = RRB3(battery_voltage, motor_voltage)

        # Switch on the LEDs
        self.rr.set_led1(self.LED_ON)
        self.rr.set_led2(self.LED_ON)

        # Turn off the open collectors
        self.rr.set_oc1(self.OC_OFF)
        self.rr.set_oc2(self.OC_OFF)

        # Turn off all the motors
        self.rr.set_motors(self.MOTOR_OFF, self.MOTOR_DIRN_FORWARD, self.MOTOR_OFF, self.MOTOR_DIRN_FORWARD)

    def move_robot(self, direction):
        '''
        Move the robot in the specified direction.
        :param direction: String of value options "F", "B", "L", "R" or "STOP".
        '''

        if direction in self.DIRN_TO_MOTOR_INPUTS.keys():
            rospy.loginfo(rospy.get_caller_id() + "Moving %s", direction)
            motor_inputs = self.DIRN_TO_MOTOR_INPUTS[direction]
            self.rr.set_motors(motor_inputs[0], motor_inputs[1], motor_inputs[2], motor_inputs[3])


def motion_topic_callback(data):
    rospy.loginfo(rospy.get_caller_id() + "Received %s", data.data)
    robotController.move_robot(data.data)


def motion_topic_listener():
    '''
    Listener for the MOTION_TOPIC which receives the control commands
    '''
    rospy.init_node('RaspiRobotV3Driver', anonymous=True)

    rospy.Subscriber("MOTION_TOPIC", String, motion_topic_callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':

    # Init the raspirobot with the right voltages
    robotController = RaspiRobot(BATTERY_VOLTAGE, MOTOR_VOLTAGE)

    motion_topic_listener()
