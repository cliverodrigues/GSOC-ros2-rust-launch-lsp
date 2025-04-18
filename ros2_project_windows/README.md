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

# Method 2: Ran on linux
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

# ROS2 Rust Launch LSP Demo

This project demonstrates a full ROS 2 application in Rust, launched using a 3-level Python launch file hierarchy. It's designed to support development of a Python-based Language Server Protocol (LSP) for ROS2 launch files.

## Features

- 🦀 Rust-based publisher/subscriber nodes
- 🧠 Launch files include rich comments for LSP feature testing:
  - Go-to-definition
  - Executable argument suggestions
  - Syntax diagnostics
  - Substitution resolution
  - Find references

## Usage

```bash
source /opt/ros/humble/setup.bash
cd ros2_ws
cargo build
ros2 launch launch/app_launch.py
