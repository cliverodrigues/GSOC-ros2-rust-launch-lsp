from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='my_rust_package',
            executable='subscriber',
            name='rust_subscriber',
            output='screen'
        )
    ])
