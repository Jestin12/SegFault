import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node

def generate_launch_description():
    ld = LaunchDescription()

    turtlebot3_bringup = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(get_package_share_directory('turtlebot3_bringup'), 'launch/robot.launch.py')
        )
    )

    camera_node = Node(
        package="camera_ros",
        executable="camera_node",
        parameters=[{
                    "camera": 0,
                    "width": 640,
                    "height": 480,
                    "format": 'BGR888',
                }]
        #ros_arguments=['format','BGR888','width','640','height','480']
    )

    test_node = Node(
        package="test_package",
        executable="testScript",
        #output='screen',
        emulate_tty=True,
        prefix="xterm -e"
    )

    ld.add_action(turtlebot3_bringup)
    ld.add_action(camera_node)
    #ld.add_action(test_node)
    
    return ld
