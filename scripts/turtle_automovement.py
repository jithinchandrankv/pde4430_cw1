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


j=rospy.init_node('turtle_automovement', anonymous=True)
rate = rospy.Rate(50)

def position(data):
    pose=data
    pose.x=round(pose.x,4)
    pose.y=round(pose.y,4)
    destination_pose.x=round(destination_pose.x,4)
    destination_pose.y=round(destination_pose.y,4)

def move(linear,angular):

    velocity.linear.x=linear
    velocity.linear.z=angular
  
def movement(pose,velocity_pub):
    
    destination_pose.x = float(input("Enter destination X coordinate: "))
    destination_pose.y = float(input("Enter destination Y coordinate: "))
    distance_tolerance=0.1
    angular_tolerance=0.0
    linear_velocity=1.5
    angular_velocity=4.0
    
    displacement = sqrt(pow(destination_pose.x - pose.x,2) + pow(destination_pose.y - pose.y,2))

    steering_angle = atan2(destination_pose.y- pose.y, destination_pose.x-pose.x) - pose.theta

    while abs(displacement) >= distance_tolerance:

            move(0,angular_velocity * steering_angle)
            if (abs(steering_angle)<=angular_tolerance):
                move(linear_velocity * displacement,0)

            rospy.loginfo("Goal has been reached")
            velocity.linear.x = 0.0
            velocity.angular.z= 0.0
            velocity_pub.publish(velocity)
            rate.sleep()
        

def autoMove():


    velocity_pub = rospy.Publisher ('turtle1/cmd_vel', Twist, queue_size=10)
    pose_subscriber=rospy.Subscriber("/turtle1/pose", pose , position )
   
    rospy.spin()


if __name__ == '__main__':
    try:
        
        autoMove()
            
    except rospy.ROSInterruptException:
        pass
    
