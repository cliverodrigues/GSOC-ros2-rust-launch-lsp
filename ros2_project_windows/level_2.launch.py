from launch import LaunchDescription
from launch.include.launch_description_source import PythonLaunchDescriptionSource
from launch.actions import IncludeLaunchDescription
import os

def generate_launch_description():
    current_dir = os.path.dirname(__file__)
    sub_sub_launch = os.path.join(current_dir, 'sub_sub_launch', 'level_3.launch.py')

    return LaunchDescription([
        # LSP Use Case: Hover support for IncludeLaunchDescription
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(sub_sub_launch)
        )
    ])
