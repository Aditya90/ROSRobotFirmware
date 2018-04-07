#!/usr/bin/env python
'''
'''
import rospy
from std_msgs.msg import String
from sensor_msgs.msg import Image, CameraInfo

import cv3
import cv3.cv as cv
import numpy as np


class ImageCapture:

    def __init__(self):
        self.node_name = 'CameraInput'

        rospy.init_node(self.node_name, anonymous=True)

        # What we do during shutdown
        # rospy.on_shutdown(self.cleanup)

        # Create the OpenCV display window for the RGB image
        self.cv_window_name = self.node_name
        cv.NamedWindow(self.cv_window_name, cv.CV_WINDOW_NORMAL)
        cv.MoveWindow(self.cv_window_name, 25, 75)

        rospy.subscriber("/cv_camera/image_raw", Image, image_capture_callback)

    def image_capture_callback(self, opencv_image):
        # Convert the image to a Numpy array since most cv2 functions
        # require Numpy arrays.
        frame = np.array(opencv_image, dtype=np.uint8)

        # Process the frame using the process_image() function
        #display_image = self.process_image(frame)
        display_image = frame
        
        # Display the image.
        cv3.imshow(self.node_name, display_image)

if __name__ == '__main__':

    # Init the raspirobot with the right voltages
    ImageCapture()

    rospy.spin()
