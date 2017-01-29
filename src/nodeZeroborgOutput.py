#!/usr/bin/env python
import rospy
from std_msgs.msg import String


def motion_topic_callback(data):
    rospy.loginfo(rospy.get_caller_id() + "Moving %s", data.data)


def motion_topic_listener():
    rospy.init_node('ZeroborgOutput', anonymous=True)

    rospy.Subscriber("MOTION_TOPIC", String, motion_topic_callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()


if __name__ == '__main__':
    motion_topic_listener()