#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
import time

class RobotController2:
    def __init__(self):
        rospy.init_node('robot_controller')
        self.cmd_vel_pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)

    def run(self):

        twist_cmd = Twist()

        
        start_time = time.time()
        rospy.loginfo("Starting rotation for 5 seconds")
        while time.time() - start_time < 5:
            elapsed_time = time.time() - start_time
            rospy.loginfo(f"Rotating... Elapsed time: {elapsed_time:.2f} seconds")
            twist_cmd.linear.x = 0
            tf = 5
            twist_cmd.angular.z = (2.76 * (tf - elapsed_time) * elapsed_time) / tf**3  
            self.cmd_vel_pub.publish(twist_cmd)
        start_time = time.time() 
        while time.time() - start_time <50:
            elapsed_time = time.time() - start_time
            rospy.loginfo(f"Moving forward... Elapsed time: {elapsed_time:.2f} seconds")
            twist_cmd.linear.x = ((36*elapsed_time)*(50-elapsed_time))/50**3
            twist_cmd.angular.z = 0
            self.cmd_vel_pub.publish(twist_cmd)
        start_time = time.time()
        rospy.loginfo("Starting rotation for 5 seconds")
        while time.time() - start_time < 5:
            elapsed_time = time.time() - start_time
            rospy.loginfo(f"Rotating... Elapsed time: {elapsed_time:.2f} seconds")
            twist_cmd.linear.x = 0
            tf = 5
            twist_cmd.angular.z = ((6*1.08) * (tf - elapsed_time) * elapsed_time) / tf**3  
            self.cmd_vel_pub.publish(twist_cmd)

if __name__ == '__main__':
    try:
        controller = RobotController2()
        controller.run()
    except rospy.ROSInterruptException:
        pass

