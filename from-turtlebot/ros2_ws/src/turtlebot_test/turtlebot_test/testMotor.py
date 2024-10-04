"""
Test Motor

Script to test the ability to send command messages to the turtlebot to control velocity.

Created: 25/06/2024
Author: Ze'ev Krischer & Michael Rubin
"""
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry


# test output to cmd_vel
class velPublisher(Node):

   def  __init__(self):
      super().__init__('vel_publisher')
      self.publisher_ = self.create_publisher(Twist, '/cmd_vel', 10)
      timer_period = 2 # seconds
      self.timer = self.create_timer(timer_period, self.timer_callback)
      self.motion = "Forward"

   def set_motion(self,motion):
      self.motion = motion
   
   def get_motion(self):
      return self.motion

   def timer_callback(self):
      msg = Twist()

      # Motion State Machine
      motion = self.get_motion()
      match motion:
         case "Forward":
            msg.linear.x = 0.05
            msg.angular.z = 0.0
            self.set_motion("Right")
         case "Right":
            msg.linear.x = 0.0
            msg.angular.z = 0.1
            self.set_motion("Left")
         case "Left":
            msg.linear.x = 0.0
            msg.angular.z = -0.1
            self.set_motion("Backward")
         case "Backward":
            msg.linear.x = -0.05
            msg.angular.z = 0.0
            self.set_motion("Stop")
         case "Stop":
            msg.linear.x = 0.0
            msg.angular.z = 0.0
            
      
      self.publisher_.publish(msg)
      self.get_logger().info('Publishing /cmd_vel: Linear =  "%f", Angular = "%f"' % (msg.linear.x,msg.angular.z))
      if (motion == "Stop"):
         raise SystemExit

   
def testMotor(args=None):
   rclpy.init(args=args)

   vel_publisher = velPublisher()
   
   try:
      rclpy.spin(vel_publisher)
   except:
      rclpy.logging.get_logger("velocity_publisher").info("Shutting down")

   vel_publisher.destroy_node()
   
   rclpy.shutdown()
      

if __name__ == '__main__':
   testMotor()

   
