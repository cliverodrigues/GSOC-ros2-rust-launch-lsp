from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import ThisLaunchFileDir
import os

def generate_launch_description():
    return LaunchDescription([
        # 🧠 LSP Use Case: Argument validation - Ensures publisher/subscriber are started correctly
        # 🧠 LSP Use Case: Substitution resolution - Helps resolve ThisLaunchFileDir at design time
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(
                os.path.join(ThisLaunchFileDir(), 'pub_launch.py')
            )
        ),
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(
                os.path.join(ThisLaunchFileDir(), 'sub_launch.py')
            )
        )
    ])
