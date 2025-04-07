from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import ThisLaunchFileDir
import os

def generate_launch_description():
    return LaunchDescription([
        # 🧠 LSP Use Case: Go to definition - Quickly navigate to orchestrator_launch.py
        # 💡 LSP Use Case: Find references - Locate where this file is included in other launch trees
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(
                os.path.join(ThisLaunchFileDir(), 'orchestrator_launch.py')
            )
        )
    ])
