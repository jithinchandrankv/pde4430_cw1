#!/usr/bin/env python3
# license removed for brevity

import rospy
import getch
from geometry_msgs.msg import Twist

pub = rospy.Publisher ('turtle1/cmd_vel', Twist, queue_size=10)

n = rospy.init_node('turtle_teleoperator',anonymous=False)
rate = rospy.Rate(10)
linear_speed=1.0
angular_speed=1.0

def initialise():
    while not rospy.is_shutdown():
        k = ord (getch.getch())
        if k==65:
            rospy.loginfo("Up")
            move_turtle(linear_speed,0.0)
        elif k==66:
            rospy.loginfo("Down")
            move_turtle(-linear_speed,0.0)
        elif k==67:
            rospy.loginfo("Right")
            move_turtle(0.0,-angular_speed)
        elif k==68:
            rospy.loginfo("Left")
            move_turtle ( 0.0,angular_speed)

def move_turtle(linear, angular):
    move_cmd = Twist()
    move_cmd.linear.x = linear
    move_cmd.angular.z = angular
    pub.publish(move_cmd)
    rate.sleep()

if __name__ == '__main__' :
    initialise ()







