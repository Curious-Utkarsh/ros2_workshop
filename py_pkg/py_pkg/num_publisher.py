#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from example_interfaces.msg import Int64
    
class NumberPublishNode(Node): 
    def __init__(self):
        super().__init__("number_publisher")
        self.number_ = 2
        self.publisher_ = self.create_publisher(Int64, "number", 10)
        self.create_timer(1.0, self.NumPublish)
        self.get_logger().info("Node Has Started")

    def NumPublish(self):
        msg = Int64()
        msg.data = int(self.number_)
        self.publisher_.publish(msg)
        self.get_logger().info(str(msg.data))

def main(args=None):
    rclpy.init(args=args)
    node = NumberPublishNode()
    rclpy.spin(node)
    rclpy.shutdown()
    
    
if __name__ == "__main__":
    main()
