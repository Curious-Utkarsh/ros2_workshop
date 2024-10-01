#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from std_srvs.srv import Empty
from py_pkg.reset_turtle import ResetTurtleNode
from time import sleep
    
class TaskNode(Node): 
    def __init__(self):
        super().__init__("move_turtle")
        self.linear_x = 0.0
        self.angular_z = 2.0
        self.dir = 1
        self.reset_ = ResetTurtleNode()
        self.publisher_ = self.create_publisher(Twist, "/turtle1/cmd_vel", 10)
        self.create_timer(1.0, self.moveCallback)
        self.get_logger().info("Node Has Started")

    def moveCallback(self):
        self.linear_x += 0.5
        if not (self.linear_x == 8.0):
            msg = Twist()
            msg.linear.x = self.linear_x
            msg.angular.z = self.angular_z * self.dir
            self.publisher_.publish(msg)
            self.get_logger().info("Linear_Vel = " + str(self.linear_x) + "  Angular_Vel = " + str(self.angular_z))
        else:
            self.get_logger().warn("Resetting Turtle in 2 seconds")
            sleep(2)
            self.reset_.reset_turtle()
            self.dir = -self.dir
            self.linear_x = 0.0




def main(args=None):
    rclpy.init(args=args)
    node = TaskNode()
    rclpy.spin(node)
    rclpy.shutdown()
    
    
if __name__ == "__main__":
    main()
