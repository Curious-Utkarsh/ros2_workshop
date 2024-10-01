#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_srvs.srv import Empty
    
class ResetTurtleNode(Node): 
    def __init__(self):
        super().__init__("reset_turtle")
        self.client = self.create_client(Empty, "/reset")
        while not self.client.wait_for_service(1):
            self.get_logger().warn("Waiting for Reset Service")
        #self.reset_turtle()

    def reset_turtle(self):
        request = Empty.Request()
        self.client.call_async(request)
        self.get_logger().info("Reset Successful")

def main(args=None):
    rclpy.init(args=args)
    node = ResetTurtleNode()
    rclpy.spin(node)
    rclpy.shutdown()
    
    
if __name__ == "__main__":
    main()
