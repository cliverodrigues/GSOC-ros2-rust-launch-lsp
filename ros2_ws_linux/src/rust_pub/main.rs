use rclrs;
use std::env;
use std_msgs::msg::String;

fn main() -> Result<(), Box<dyn std::error::Error>> {
    let context = rclrs::Context::new(std::env::args())?;
    let node = rclrs::create_node(&context, "rust_publisher")?;
    let publisher = node.create_publisher::<String>("custom_topic", rclrs::QOS_PROFILE_DEFAULT)?;

    // Get parameters from CLI
    let args: Vec<String> = env::args().collect();
    let data = format!(
        "Params: {}, {}, {}, {}, {}",
        args.get(1).unwrap_or(&"p1".into()),
        args.get(2).unwrap_or(&"p2".into()),
        args.get(3).unwrap_or(&"p3".into()),
        args.get(4).unwrap_or(&"p4".into()),
        args.get(5).unwrap_or(&"p5".into())
    );

    loop {
        let msg = String { data: data.clone() };
        publisher.publish(msg)?;
        std::thread::sleep(std::time::Duration::from_secs(1));
    }
}
