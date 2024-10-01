SETTING UP THE TURTLEBOT



1. GENERAL NOTES: 

Two machines: laptop, computer on turtlebot
Both machines need to have the same ROS_DOMAIN_ID (should be set to 9) to connect 

2. SOURCE THE LAPTOP 




3. SETTING UP THE TURTLEBOT 

ssh ubuntu@10.42.0.1
Password = turtlebot



4. SELF_TEST

If wanted to test launch and camera:

-	selfTest
Input number corresponding to node that you want to test 

-	finding the launch file:
You can search through the files in the turtlebot as you would on your computer

the file: 
self_test.launch.py 

is in:
cd ~/ros2_ws/install/self_test/share/self_test/launch

5. TELEOP (MOVING TURTLEBOT USING YOU KEYBOARD)

-	If wanted to test teleop on actual turtlebot:

In a new terminal (turtlebot machine)

	Ros2 launch turtlebot_test self_test.launch.py

In new terminal (turlebot machine)

	export TURTLEBOT3_MODEL=burger 
	Ros2 run turtlebot3_teleop teleop_keyboard
	
	
5. MAKING PUBLISHERS

	#include "rclcpp/rclcpp.hpp"
	#include "geometry_msgs/msg/pose.hpp"

	class AutoPilotNode : public rclcpp::Node {
		public:
			AutoPilotNode() : Node("autopilot") 
			{
				publisher = create_publisher<geometry_msgs::msg::Pose>("flight/waypoints", 10);
				timer = create_wall_timer(std::chrono::milliseconds(1000),
				std::bind(&AutoPilotNode::PublishWaypoints, this));
				RCLCPP_INFO(get_logger(), "Autopilot has been started");
			}
		
		private:
			void PublishWaypoints() {
				geometry_msgs::msg::Pose msg =
				geometry_msgs::msg::Pose();
				msg.position.x = 1.0;
				msg.position.y = 2.0;
				msg.orientation.w = 1.0;
				RCLCPP_INFO(get_logger(), "Sending pose x: %f y: %f", msg.position.x, msg.position.y);
				publisher->publish(msg);
			}
			rclcpp::Publisher<geometry_msgs::msg::Pose>::SharedPtr publisher;
			rclcpp::TimerBase::SharedPtr timer;
	};

6. MAKING SUBSCRIBERS

	#include "rclcpp/rclcpp.hpp"
	#include "geometry_msgs/msg/pose.hpp"

	class MotionControlNode : public rclcpp::Node {
		public:
			MotionControlNode(): Node("motion_control") 
			{
				subscriber = create_subscription<geometry_msgs::msg::Pose>("flight/waypoints", 10,
				std::bind(&MotionControlNode::callback, this, std::placeholders::_1));
				RCLCPP_INFO(get_logger(), "Motion Controller active");
			}
		private:
			void callback(const geometry_msgs::msg::Pose::SharedPtr msg) 
			{
				RCLCPP_INFO(get_logger(), "Received x: %f, y: %f", msg->position.x, msg->position.y);
				// Some actual motion control code
			}
			rclcpp::Subscription<geometry_msgs::msg::Pose>::SharedPtr subscriber;
	};


7. Callbacks

	Two kinds of callbacks: 	FUNCTION AND CLASS METHOD

	-	FUNCTION

	void callback(const std_msgs::msg::String::SharedPtr msg)
	{
		// ...
	}
	rclcpp::Subscription<std_msgs::msg::String>::SharedPtr subscriber;
	subscriber = node->create_subscription<std_msgs::msg::String>("my_topic", 1, callback);

8. INCLUDE PATHS

When including a header file, include this way:

#include "../include/TBmain.hpp"        //relative include path


Also, to include a directory through a CMakeLists.txt, write this:

include_directories(
  "${CMAKE_SOURCE_DIR}/include"
)

Include in both ways for redundancy, it works without raising any redefinition errors.

I've found it can get rid of this error, although unreliably you need to play around with the include options:

CMake Warning (dev) at /usr/share/cmake-3.22/Modules/FindPackageHandleStandardArgs.cmake:438 (message):
  The package name passed to `find_package_handle_standard_args` (PkgConfig)
  does not match the name of the calling package (gazebo).  This can lead to
  problems in calling code that expects `find_package` result variables
  (e.g., `_FOUND`) to follow a certain pattern.
Call Stack (most recent call first):
  /usr/share/cmake-3.22/Modules/FindPkgConfig.cmake:99 (find_package_handle_standard_args)
  /usr/lib/x86_64-linux-gnu/cmake/gazebo/gazebo-config.cmake:72 (include)
  CMakeLists.txt:23 (find_package)
This warning is for project developers.  Use -Wno-dev to suppress it.


9.


 

