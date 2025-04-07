// src/subscriber.rs
use rclrs::{Context, Node};
use std::fs::OpenOptions;
use std::io::Write;

fn main() -> Result<(), Box<dyn std::error::Error>> {
    let context = Context::new(std::env::args())?;
    let node = Node::new(&context, "rust_subscriber_node")?;

    let file_path = "/tmp/ros2_output.txt";
    let mut file = OpenOptions::new().append(true).create(true).open(file_path)?;

    let _subscription = node.create_subscription::<std_msgs::msg::String>(
        "topic1",
        rclrs::QOS_PROFILE_DEFAULT,
        move |msg| {
            let extracted = &msg.data; // In practice, parse needed params
            writeln!(file, "Received: {}", extracted).unwrap();
        },
    )?;

    rclrs::spin(&node)?;
    Ok(())
}
