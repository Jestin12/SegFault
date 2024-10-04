"""
Self Test Script

Script to test the all functionality from the turtlebot

Created: 18/07/2024
Author: Ze'ev Krischer & Michael Rubin
# """

from . import testCamera
from . import testLED
from . import testScan
from . import testMotor

import rclpy
from rclpy.node import Node
import os
import signal
from rcl_interfaces.msg import Log


class Tester(Node):
    def __init__(self):
        super().__init__('log_subscriber')

        self.subscription = self.create_subscription(Log, "/rosout", self.callback, 1)
        self.subscription

        self.testTime = False

    def set_testTime(self,testTime):
      self.testTime = testTime
   
    def get_testTime(self):
      return self.testTime

    def callback(self, ros_data):
        print("I work!")
        if (ros_data.msg == "Run!" and ros_data.name == "diff_drive_controller"):
            self.set_testTime(True)  

    def testAll():
        testMotor.testMotor()
        testLED.testLED()
        testScan.testScan()
        testCamera.testCamera()


def main(args=None):
    rclpy.init(args=args)

    tester = Tester()
    while(1):
        print(tester.get_testTime())
        if (tester.get_testTime()):

            print("\033[1m" + "Time to test!\n" + "Input the corresponding number to undergo that test" + "\033[0m")
            print("1. Test Motors\n2. Test LED\n3. Test Lidar\n4. Test Camera\n5. Test All\n\nIf you'd like to quit, make sure to hit ctrl+c")
            option = input()

            match option:
                case "1":
                    testMotor.testMotor()
                case "2":
                    testLED.testLED()
                case "3":
                    testScan.testScan()
                case "4":
                    testCamera.testCamera()
                case "5": 
                    tester.testAll()
        else:
            rclpy.spin_once(tester)

    rclpy.shutdown()
            

if __name__ == '__main__':
    main()
