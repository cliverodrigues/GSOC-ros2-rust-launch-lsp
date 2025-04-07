// src/publisher.rs
use rclrs::{Context, Node};
use std::error::Error;

fn main() -> Result<(), Box<dyn Error>> {
    let context = Context::new(std::env::args())?;
    let node = Node::new(&context, "rust_publisher_node")?;

    let publisher = node.create_publisher::<std_msgs::msg::String>("topic1", rclrs::QOS_PROFILE_DEFAULT)?;

    std::thread::spawn(move || loop {
        let msg = std_msgs::msg::String {
            data: format!(
                "param1: {}, param2: {}, param3: {}, param4: {}, param5: {}",
                1, 2, 3, 4, 5
            ),
        };
        publisher.publish(msg).unwrap();
        std::thread::sleep(std::time::Duration::from_secs(1));
    });

    rclrs::spin(&node).unwrap();
    Ok(())
}
