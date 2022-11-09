#!/usr/bin/env python
# license removed for brevity

import rospy
import getch
from geometry_msgs.msg import Twist

pub = rospy.Publisher ('turtle/cmd_vel',Twist,queue_size=1)

n=rospy.init_node('turtle_teleoperator',anonymous=False)
rate = rospy.rate(10)
linear_speed=0.1
angular_speed=1.0
