from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='rust_pub',
            executable='rust_pub',
            name='rust_publisher',
            # 🧠 LSP Use Case: Executable argument suggestions - Helps autocomplete args
            arguments=['alpha', 'beta', 'gamma', 'delta', 'epsilon']
        )
    ])
