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

selfTest
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







 

