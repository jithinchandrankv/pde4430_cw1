#!/usr/bin/env python3
# license removed for brevity

import rospy
import getch
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
from math import pow, atan2, sqrt


pose = Pose()
destination_pose = Pose()
velocity=Twist()

pub = rospy.Publisher ('turtle1/cmd_vel', Twist, queue_size=10)



def callback(data):

    pose=data



def automovement():
    destination_pose = Pose()

    rospy.init_node('turtle_automovement', anonymous=True)
    
    rospy.Subscriber("/turtle1/pose", Pose , callback)
    rate = rospy.Rate(10)
    
    user_input = input("Enter goal coordinates in x,y format: ")
    destination_tolerance = input("tolerance: ")
    tokens = user_input.split(",", 1)
    x_coordinate = tokens[0]
    y_coordinate = tokens[1]

    print(x_coordinate)
    print(y_coordinate)
    
