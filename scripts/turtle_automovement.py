#!/usr/bin/env python3
# license removed for brevity

import rospy
import getch
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
from math import pow, atan2, sqrt


def automovement(self):
    goal_pose = Pose()
    user_input = input("Enter goal coordinates in x,y format: ")
    tokens = user_input.split(",", 1)
    x_coordinate = tokens[0]
    y_coordinate = tokens[1]
    print(x_coordinate)
    print(y_coordinate)

