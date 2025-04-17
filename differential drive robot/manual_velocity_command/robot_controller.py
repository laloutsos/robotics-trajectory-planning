#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
import time  

class RobotController:
    def __init__(self):
        rospy.init_node('robot_controller')
        self.cmd_vel_pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)

    def run(self):
        rate = rospy.Rate(10)  # 10 Hz
        twist_cmd = Twist()


        start_time = time.time()  
        rospy.loginfo("Starting rotation for 10 seconds")
        while time.time() - start_time < 10:
            elapsed_time = time.time() - start_time
            rospy.loginfo(f"Rotating... Elapsed time: {elapsed_time:.2f} seconds")
            twist_cmd.linear.x = 0
            twist_cmd.angular.z = -0.2618  
            self.cmd_vel_pub.publish(twist_cmd)
            rate.sleep()


        start_time = time.time()  
        rospy.loginfo("Starting forward movement for 15 seconds")
        while time.time() - start_time < 15:
            elapsed_time = time.time() - start_time
            rospy.loginfo(f"Moving forward... Elapsed time: {elapsed_time:.2f} seconds")
            twist_cmd.linear.x = 0.1
            twist_cmd.angular.z = 0.1745  
            self.cmd_vel_pub.publish(twist_cmd)
            rate.sleep()

        rospy.loginfo("Stopping the robot")


        twist_cmd.linear.x = 0
        twist_cmd.angular.z = 0
        self.cmd_vel_pub.publish(twist_cmd)

if __name__ == '__main__':
    try:
        controller = RobotController()
        controller.run()
    except rospy.ROSInterruptException:
        pass

