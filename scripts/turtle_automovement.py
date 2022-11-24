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
    destination_pose = Pose()
    velocity=Twist()
   
    
def movement(PoseData,velocity):
    
    destination_tolerance = input("tolerance: ")
    displacement = sqrt(pow(destination_pose.x - Pose.x,2) + pow(destination_pose.y - Pose.y,2))
    steering_angle = atan2(destination_pose.y- Pose.y, destination_pose.x-Pose.x) - Pose.theta

    while displacement >= destination_tolerance:

        steering_angle = abs(atan2(destination_pose.y-Pose.y, destination_pose.x-Pose.x) - Pose.theta)
        velocity.linear.x = 0.0
        velocity.angular.z = steering_angle *0.4

    if displacement>0.2:
        velocity.angular.z = atan2(destination_pose.y-Pose.y, destination_pose.x-Pose.x) - Pose.theta
        velocity.linear.x = displacement * 0.2
       
        pub.publish(velocity)

    else:
        velocity.angular.z = 0
        velocity.linear.x = 0
        
        pub.publish(velocity)

def autoMove():

    rospy.init_node('turtlebolt_controller', anonymous=True)

    rospy.Subscriber("/turtle1/pose", Pose , callback,movement)

    rate = rospy.Rate(10)
    
    destination_pose.x = float(input("Enter destination X coordinate: "))
    destination_pose.y = float(input("Enter destination Y coordinate: "))

    rospy.spin()


if __name__ == '__main__':
    try:

        autoMove()
            
    except rospy.ROSInterruptException:
        pass
    
