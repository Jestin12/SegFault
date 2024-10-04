"""
Test Camera (Image)

Script to test the ability to recieve and interpret image messages from the turtlebot

Created: 18/07/2024
Author: Ze'ev Krischer & Michael Rubin
# """
import sys, time

import numpy as np

import cv2

import rclpy
from rclpy.node import Node

import rclpy.subscription
from sensor_msgs.msg import Image, CompressedImage

import os

VERBOSE = True

class imageSubscriber(Node):
    def __init__(self):
        super().__init__('image_subscriber')

        self.subscription = self.create_subscription(CompressedImage, "/camera/image_raw/compressed", self.callback, 1)
        self.subscription
        if VERBOSE :
            print("subscribed to /camera/image_raw/compressed")

    def callback(self, ros_data):

        np_arr = np.array(ros_data.data, np.uint8)
        image_np = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)

        if not cv2.imwrite(os.path.join(os.path.expanduser('~'),'ros2_ws','test_package','testImages','test.jpg'), image_np):
            raise Exception("Could not write image")
        
        print("Photo has been recorded and will be displayed via text")
        # raise SystemExit


def testCamera(args=None):
    # rclpy.init(args=args)

    image_subscriber = imageSubscriber()
    rclpy.spin_once(image_subscriber)    
    # try:
        
    #     rclpy.spin(image_subscriber)
    # except SystemExit:
    #     rclpy.logging.get_logger("image_subscriber").info("Shutting down")

    image_subscriber.destroy_node()
    # rclpy.shutdown()
    os.system('tiv ~/ros2_ws/test_package/testImages/test.jpg')

if __name__ == '__main__':
    testCamera()