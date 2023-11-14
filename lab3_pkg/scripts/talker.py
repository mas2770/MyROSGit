#!/usr/bin/env python3
import rospy
from std_msgs.msg import String

rospy.init_node('talker')
pub1 = rospy.Publisher('time_topic', String, queue_size=10)
pub2 = rospy.Publisher('overflow_topic', String, queue_size=10)
rate = rospy.Rate(10)

def start_talker():
    msg1 = String()
    msg2 = String()
    num = 0
    while not rospy.is_shutdown():
    	num += 2
    	if num == 100:
    		num = 0
    		msg2.data = "OverFlow!!!"
    		pub2.publish(msg2)
    	even_num = str(num)
    	rospy.loginfo(even_num)

    	msg1.data = even_num
    	pub1.publish(msg1)

    	rate.sleep()

try:
    start_talker()
except (rospy.ROSInterruptException, KeyboardInterrupt):
    rospy.logerr('Exception catched')
