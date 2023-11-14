#!/usr/bin/env python3
import rospy
from std_msgs.msg import String

def callback(msg):
    rospy.loginfo("I heard %s", msg.data)

rospy.init_node('listener_1')
rospy.Subscriber('time_topic', String, callback, queue_size=10)
rospy.spin()
