"""
Test Scan

Script to test the ability to recieve and interpret scan messages from the turtlebot

Created: 25/06/2024
Author: Ze'ev Krischer & Michael Rubin
"""
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import LaserScan
from rclpy.qos import QoSProfile, QoSReliabilityPolicy, QoSHistoryPolicy, QoSPresetProfiles, qos_profile_sensor_data


# test output to cmd_vel
class scanSubscriber(Node):

   def  __init__(self):
      super().__init__('scan_subscriber')

      self.subscription = self.create_subscription(
         LaserScan,
         '/scan',
         self.listener_callback,
         qos_profile= qos_profile_sensor_data)
      self.subscription
      
   def listener_callback(self, msg):
      scan_angle = {0, 90, 180, 270}

      self.get_logger().info('Scan Readings at 0: %f, 90: %f, 180: %f, 270: %f\n' % (msg.ranges[0],msg.ranges[90],msg.ranges[180],msg.ranges[270]))

   
def testScan(args=None):
   rclpy.init(args=args)

   scan_subscriber = scanSubscriber()
   scan_count = 0
   # try:
   #    rclpy.spin(scan_subscriber)
   # except SystemExit:
   #    rclpy.logging.get_logger("scan_subscriber").info("Shutting down")
   while (scan_count < 4):
      match scan_count:
         case 0:
            print("Put your hand in front of the robot")
         case 1:
            print("Put your hand to the left of the robot")
         case 2:
            print("Put your hand behind the robot")
         case 3:
            print("Put your hand to the right of the robot")

      input("Hit Enter When Ready\n")
      
      rclpy.spin_once(scan_subscriber)
      scan_count +=1
   scan_subscriber.destroy_node()
   rclpy.shutdown()

if __name__ == '__main__':
   testScan()

   
