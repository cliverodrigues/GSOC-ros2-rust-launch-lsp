from launch import LaunchDescription
from launch.include.launch_description_source import PythonLaunchDescriptionSource
from launch.actions import IncludeLaunchDescription
import os

def generate_launch_description():
    base_dir = os.path.join(os.path.dirname(__file__), 'sub_launch', 'level_2.launch.py')
    return LaunchDescription([
        # LSP Use Case: Error squiggles for incorrect relative pathing
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(base_dir)
        )
    ])
