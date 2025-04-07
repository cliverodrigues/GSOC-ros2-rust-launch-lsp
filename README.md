# ROS2 Rust Nodes with Python Launch LSP

# Launch Files Directory Structure
'''
ros2_project/
├── launch/
│   ├── level_1_entrypoint.launch.py
│   └── sub_launch/
│       ├── level_2.launch.py
│       └── sub_sub_launch/
│           ├── level_3.launch.py
│           ├── publisher_launch.py
│           └── subscriber_launch.py

Method 2
ros2_ws/
├── src/
│   ├── rust_pub/
│   │   ├── Cargo.toml
│   │   └── src/
│   │       └── main.rs               # Publisher Node
│   └── rust_sub/
│       ├── Cargo.toml
│       └── src/
│           └── main.rs               # Subscriber Node
├── launch/
│   ├── app_launch.py                 # Level 1 (entry point)
│   ├── orchestrator_launch.py        # Level 2
│   ├── pub_launch.py                 # Level 3 (publisher node)
│   └── sub_launch.py                 # Level 3 (subscriber node)
├── CMakeLists.txt                    # If you're using CMake for the ROS2 build
├── package.xml                       # Optional for ROS2 package discovery
├── .gitignore
└── README.md
