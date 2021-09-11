#!/usr/bin/env python

import rospy, math, copy
from std_msgs.msg import Int32MultiArray

def callback(msg):
    xycar_msg = Int32MultiArray()
    angle = 0
    fl = msg.data[0]
    fm = msg.data[1]
    fr = msg.data[2]
    r = msg.data[6]
    l = msg.data[7]
    if fl < 240 and fr > 120:
        xycar_msg.data = [50, 100]
    elif fl > 120:
        xycar_msg.data = [-50, 100]
    else:
        xycar_msg.data = [angle, 100]
    motor_pub.publish(xycar_msg)
rospy.init_node('guide')
motor_pub = rospy.Publisher('xycar_motor_msg', Int32MultiArray, queue_size=1)
ultra_sub = rospy.Subscriber('ultrasonic', Int32MultiArray, callback)
rospy.spin()
