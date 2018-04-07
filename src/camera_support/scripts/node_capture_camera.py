#!/usr/bin/env python
'''
'''
import rospy
from std_msgs.msg import String
from sensor_msgs.msg import Image, CameraInfo

import cv2
#import cv2.cv as cv
import numpy as np


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

        rospy.Subscriber("/cv_camera/image_raw", String, self.image_capture_callback)

    def image_capture_callback(self, opencv_image):
        # Convert the image to a Numpy array since most cv2 functions
        # require Numpy arrays.
        frame = np.array(opencv_image, dtype=np.uint8)

        # Process the frame using the process_image() function
        #display_image = self.process_image(frame)
        display_image = frame
        
        # Display the image.
        cv2.imshow(self.node_name, display_image)

if __name__ == '__main__':

    # Init the raspirobot with the right voltages
    ImageCapture()

    rospy.spin()
