import rospy
from std_msgs.msg import Float64
import time

def main():
    rospy.init_node('move_rrbot', anonymous=True)
    
    
    pub1 = rospy.Publisher('/rrbot/joint1_position_controller/command', Float64, queue_size=10)
    pub2 = rospy.Publisher('/rrbot/joint2_position_controller/command', Float64, queue_size=10)

  
    tf = 20
    tb = 2
    a1 = 0.032
    a2 = -0.02



    start_time = time.time()

    while not rospy.is_shutdown():
        elapsed_time = time.time() - start_time
        
        if elapsed_time < tb:
            joint1_velocity = (1/2)*a1*(elapsed_time)**2
            joint2_velocity = (1/2)*a2*(elapsed_time)**2
        elif elapsed_time < tf - tb:
            joint1_velocity = (1/2)*a1*(tb**2) + a1*tb*(elapsed_time-tb)
            joint2_velocity = (1/2)*a2*(tb**2) + a2*tb*(elapsed_time-tb)
        elif elapsed_time < tf:
            joint1_velocity = 1.17 - (1/2)*a1*((tf-elapsed_time)**2)
            joint2_velocity = -0.78 - (1/2)*a2*((tf-elapsed_time)**2)
        else:
            break


        pub1.publish(Float64(joint1_velocity))
        pub2.publish(Float64(joint2_velocity))

        rospy.sleep(0.1)  

if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass

