#!/usr/bin/env python3
import rospy
from std_msgs.msg import String

rospy.init_node('talker')
pub1 = rospy.Publisher('topic_1', String, queue_size=10, latch = True)
rate = rospy.Rate(10)

def start_talker():
    
    num1 = rospy.get_param('/talker/num_1')
    num2 = rospy.get_param('/talker/num_2')
    num3 = rospy.get_param('/talker/num_3')
    add = String()
    add = str(num1)+" "+str(num2)+" "+str(num3)
    
    	
    rospy.loginfo(add)
    pub1.publish(add)
    	
    rate.sleep()

try:
    start_talker()
except (rospy.ROSInterruptException, KeyboardInterrupt):
    rospy.logerr('Exception catched')
