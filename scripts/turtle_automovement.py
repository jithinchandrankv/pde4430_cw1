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

velocity_pub = rospy.Publisher ('turtle1/cmd_vel', Twist, queue_size=10)

j=rospy.init_node('turtle_automovement', anonymous=True)
rate = rospy.Rate(50)

def position():
    pose.x=round(pose.x,4)
    pose.y=round(pose.y,4)
    destination_pose.x=round(destination_pose.x,4)
    destination_pose.y=round(destination_pose.y,4)
  
def movement(pose,velocity_pub):
    
    destination_pose.x = float(input("Enter destination X coordinate: "))
    destination_pose.y = float(input("Enter destination Y coordinate: "))
    
    displacement = sqrt(pow(destination_pose.x - pose.x,2) + pow(destination_pose.y - pose.y,2))

    steering_angle = atan2(destination_pose.y- pose.y, destination_pose.x-pose.x) - pose.theta

    while abs(displacement)>= 0.1:
        velocity.linear.x = 0.0
        velocity.angular.z = steering_angle *4
        velocity_pub.publish(velocity)
        rate.sleep()
        if round(steering_angle,2)<=0.0:
        
            velocity.linear.x = displacement * 1.5
            velocity.angular.z = 0.0
            velocity_pub.publish(velocity)
            rate.sleep()

    
    else:
        velocity.angular.z = 0
        velocity.linear.x = 0
        print ("displacement: reached")
        velocity_pub.publish(velocity)
        rospy.sleep()

        

def autoMove():


    velocity_pub = rospy.Publisher ('turtle1/cmd_vel', Twist, queue_size=10)
    pose_subscriber=rospy.Subscriber("/turtle1/pose", pose , movement )
   
    rospy.spin()


if __name__ == '__main__':
    try:
        
        autoMove()
            
    except rospy.ROSInterruptException:
        pass
    
