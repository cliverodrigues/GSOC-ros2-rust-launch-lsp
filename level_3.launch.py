from launch import LaunchDescription
from launch.include.launch_description_source import PythonLaunchDescriptionSource
from launch.actions import IncludeLaunchDescription
import os

def generate_launch_description():
    current_dir = os.path.dirname(__file__)
    
    return LaunchDescription([
        # LSP Use Case: Supports cross-reference navigation to submodules
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(os.path.join(current_dir, 'publisher_launch.py'))
        ),
        # LSP Use Case: Allows hover info and signature help on action setup
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(os.path.join(current_dir, 'subscriber_launch.py'))
        ),
    ])
