#!/usr/bin/env python3
# license removed for brevity

import rospy
import getch
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose

def callback (data):
    rospy. loginfo("x = %f" % data.x)
    rospy.loginfo("y = %f" % data.y )

    if ((data.x <= 0.5 or data.y ==10.0)):

        rospy. loginfo("turtle hit the wall")

    elif (( data.x >=11.0 or data.y <= 0.5)):

        rospy. loginfo("turtle hit the wall")

    elif (data.x == 0.015 and data.y == 0.05):

        rospy. loginfo("turtle hit the wall")

    elif (data.x >= 11.0 and data.y >= 11.0):

        rospy. loginfo("turtle hit the wall")



if __name__ == '__main__' :
   