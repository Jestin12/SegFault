SETTING UP THE TURTLEBOT



1. GENERAL NOTES: 

Two machines: laptop, computer on turtlebot
Both machines need to have the same ROS_DOMAIN_ID (should be set to 9) to connect 

2. SOURCE THE LAPTOP 




3. SETTING UP THE TURTLEBOT 

ssh ubuntu@10.42.0.1
Password = turtlebot



If wanted to test launch and camera:

selfTest
Input number corresponding to node that you want to test 

If wanted to test teleop 

Ros2 launch turtlebot_test self_test.launch.py

In new terminal (laptop machine)

export TURTLEBOT3_MODEL=burger 
Ros2 run turtlebot3_teleop teleop_keyboard







 

