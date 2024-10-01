#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
    
class MoveTurtleNode(Node): 
    def __init__(self):
        super().__init__("move_turtle")
        self.linear_x = 0.0
        self.angular_z = 2.0
        self.publisher_ = self.create_publisher(Twist, "/turtle1/cmd_vel", 10)
        self.create_timer(1.0, self.moveCallback)
        self.get_logger().info("Node Has Started")

    def moveCallback(self):
        self.linear_x += 0.5
        msg = Twist()
        msg.linear.x = self.linear_x
        msg.angular.z = -self.angular_z
        self.publisher_.publish(msg)
        self.get_logger().info("Linear_Vel = " + str(self.linear_x) + "  Angular_Vel = " + str(self.angular_z))

def main(args=None):
    rclpy.init(args=args)
    node = MoveTurtleNode()
    rclpy.spin(node)
    rclpy.shutdown()
    
    
if __name__ == "__main__":
    main()
