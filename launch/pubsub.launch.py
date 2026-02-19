from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription(
        [
            # Add talker node with message_prefix parameter
            Node(
                package='ros2_launch_demo',
                executable='talker',
                name='talker',
                parameters=[
                    {'message_prefix': 'ROS2'}
                ]
            ),
            
            # Add listener node
            Node(
                package='ros2_launch_demo',
                executable='listener',
                name='listener'
            )
        ]
    )