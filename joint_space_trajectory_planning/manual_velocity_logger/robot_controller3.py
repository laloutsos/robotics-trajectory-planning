#!/usr/bin/env python

import rospy
from std_msgs.msg import Float64
import time

def main():
    rospy.init_node('move_rrbot', anonymous=True)
    

    pub1 = rospy.Publisher('/rrbot/joint1_position_controller/command', Float64, queue_size=10)
    pub2 = rospy.Publisher('/rrbot/joint2_position_controller/command', Float64, queue_size=10)


    final_angles = [25.0 * (3.14159 / 180.0), -30.0 * (3.14159 / 180.0)]  

    rospy.loginfo("Moving to final angles...")
    
    start_time = time.time()
    duration = 5  

    while not rospy.is_shutdown():
        current_time = time.time()
        elapsed_time = current_time - start_time
        
        if elapsed_time > duration:
            rospy.loginfo("Reached final angles. Exiting...")
            break
        

        pub1.publish(Float64(final_angles[0]))

        pub2.publish(Float64(final_angles[1]))

        time.sleep(0.1)  

if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass

