cmake_minimum_required(VERSION 3.5)
project(ros2_rust_launch_demo)

# Required for ROS 2
find_package(ament_cmake REQUIRED)

# If you had any build steps, you could include them here
# But since Rust uses Cargo, we skip actual building here

ament_package()
