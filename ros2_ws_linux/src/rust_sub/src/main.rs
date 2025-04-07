use rclrs;
use std::fs::OpenOptions;
use std::io::Write;
use std::env;
use std_msgs::msg::String;

fn main() -> Result<(), Box<dyn std::error::Error>> {
    let context = rclrs::Context::new(std::env::args())?;
    let node = rclrs::create_node(&context, "rust_subscriber")?;

    let output_path = env::args().nth(1).unwrap_or("output.txt".to_string());
    let prefix = env::args().nth(2).unwrap_or("Received".to_string());

    let _subscription = node.create_subscription::<String, _>(
        "custom_topic",
        rclrs::QOS_PROFILE_DEFAULT,
        move |msg| {
            let mut file = OpenOptions::new().create(true).append(true).open(&output_path).unwrap();
            writeln!(file, "{}: {}", prefix, msg.data).unwrap();
        },
    )?;

    rclrs::spin(&node)?;
    Ok(())
}
