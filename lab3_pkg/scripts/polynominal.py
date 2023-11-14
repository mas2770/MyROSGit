#!/usr/bin/env python3

import rospy
from std_msgs.msg import String


def callback(msg):
    new_message = msg.data
    pub = rospy.Publisher('topic_2', String, queue_size=10)
    msgArr = new_message.split(" ")
    num1 = float(msgArr[0])
    num2 = float(msgArr[1])**2
    num3 = float(msgArr[2])**3
    
    msgRes = str(num3) + " "+ str(num2)+" "+str(num1)
    pub.publish(msgRes)
    rate.sleep()

rospy.init_node('tl')
rate = rospy.Rate(10)
rospy.Subscriber('topic_1', String, callback, queue_size=10)
rospy.spin()


