from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='rust_sub',
            executable='rust_sub',
            name='rust_subscriber',
            arguments=['/tmp/output.txt', 'Logged'],
            # 🧠 LSP Use Case: Code completion for Node() args like `arguments`, `name`, etc.
        )
    ])
