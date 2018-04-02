#!/usr/bin/env python
'''
This node is a subscriber to print out everything which is going on the Motion Topic.
It is merely for validation of the pub-sub method (as an alternative to opening up
the raw ros topic).
'''
import rospy
from std_msgs.msg import String


def motion_topic_callback(data):
    rospy.loginfo(rospy.get_caller_id() + "Moving %s", data.data)


def motion_topic_listener():
    rospy.init_node('MotionTopicSubscriber', anonymous=True)

    rospy.Subscriber("MOTION_TOPIC", String, motion_topic_callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()


if __name__ == '__main__':
    motion_topic_listener()
