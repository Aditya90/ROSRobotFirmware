#!/usr/bin/env python
'''
'''
import rospy
from std_msgs.msg import String

def motion_topic_callback(data):
    rospy.loginfo(rospy.get_caller_id() + "Received %s", data.data)
    robotController.move_robot(data.data)


def motion_topic_listener():
    '''
    Publisher for the CAMERA_TOPIC which sends the inputs from the camera
    '''
    rospy.init_node('CameraInput', anonymous=True)

    rospy.subscriber("CAMERA_TOPIC", String, queue_size=2)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':

    # Init the raspirobot with the right voltages
    robotController = RaspiRobot(BATTERY_VOLTAGE, MOTOR_VOLTAGE)

    motion_topic_listener()
