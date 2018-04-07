#!/usr/bin/env python
'''
'''
import rospy
from std_msgs.msg import String
from sensor_msgs.msg import Image, CameraInfo

import cv2
#import cv2.cv as cv
import numpy as np
from cv_bridge import CvBridge, CvBridgeError


class ImageCapture:

    def __init__(self):
        self.node_name = 'CameraInput'

        rospy.init_node(self.node_name, anonymous=True)

        # What we do during shutdown
        # rospy.on_shutdown(self.cleanup)

        # Create the OpenCV display window for the RGB image
        self.cv_window_name = self.node_name
        cv2.namedWindow(self.cv_window_name, cv2.WINDOW_NORMAL)
        cv2.moveWindow(self.cv_window_name, 25, 75)
        # Create the cv_bridge object
        self.bridge = CvBridge()

        self.image_sub = rospy.Subscriber("/cv_camera/image_raw", Image, self.image_capture_callback)

    def image_capture_callback(self, opencv_image):
        # Use cv_bridge() to convert the ROS image to OpenCV format
        try:
            frame = self.bridge.imgmsg_to_cv2(opencv_image, "bgr8")
        except CvBridgeError, e:
            print e

        # Convert the image to a Numpy array since most cv2 functions
        # require Numpy arrays.
        frame = np.array(frame, dtype=np.uint8)

        # Process the frame using the process_image() function
        display_image = self.process_image(frame)

        # Display the image.
        cv2.imshow(self.node_name, display_image)

    def process_image(self, frame):
        # Convert to greyscale
        grey = cv2.cvtColor(frame, cv2.BGR2GRAY)

        # Blur the image
        grey = cv2.blur(grey, (7, 7))

        # Compute edges using the Canny edge filter
        edges = cv2.Canny(grey, 15.0, 30.0)

        return edges

if __name__ == '__main__':

    # Init the raspirobot with the right voltages
    ImageCapture()

    rospy.spin()
