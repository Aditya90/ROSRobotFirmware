#!/usr/bin/env python
'''
The main control input. This node gets inputs from the keyboard
and redirects it to the ROS topic.
'''

import rospy
from std_msgs.msg import String


def keyboard_controller():
    pub = rospy.Publisher('MOTION_TOPIC', String, queue_size=2)
    rospy.init_node('KeyboardController', anonymous=True)
    while not rospy.is_shutdown():
        motion_topic_arg = raw_input('What direction do you wish to move? (F,L,R,B,S) : ')
        motion_topic_str = "%s" % motion_topic_arg
        rospy.loginfo(motion_topic_str)
        pub.publish(motion_topic_str)


if __name__ == '__main__':
    try:
        keyboard_controller()
    except rospy.ROSInterruptException:
        pass
