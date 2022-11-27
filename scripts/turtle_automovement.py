#!/usr/bin/env python3


import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
from math import pow, atan2, sqrt


class autonavigation:

    def __init__(self):
        rospy.init_node('turtle_automovement', anonymous=True)
        self.velocity_publisher= rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
        self.pose_subscriber = rospy.Subscriber('/turtle1/pose', Pose, self.position)
        self.pose=Pose()
        self.rate = rospy.Rate(10)
        

    def position(self,data):
      
        self.pose = data
        self.pose.x=round(self.pose.x,4)
        self.pose.y=round(self.pose.y,4)

    def distance(self,destination_pose):
        distance = sqrt(pow(destination_pose.x - self.pose.x,2) + pow(destination_pose.y - self.pose.y,2))
        return distance


    def movement(self): 

    
        distance_tolerance = 0.1
        vel_command= Twist()

        destination_pose=Pose()

        destination_pose.x = float(input("Enter destination X coordinate: "))
        
        destination_pose.y = float(input("Enter destination Y coordinate: "))


        distance = sqrt(pow(destination_pose.x - self.pose.x,2) + pow(destination_pose.y - self.pose.y,2))

        steering_angle = atan2(destination_pose.y- self.pose.y, destination_pose.x- self.pose.x) - self.pose.theta
        
        while distance>=distance_tolerance:

            vel_command.linear.x= 1.5*sqrt(pow(destination_pose.x - self.pose.x,2) + pow(destination_pose.y - self.pose.y,2))
            vel_command.angular.z= 4*(atan2(destination_pose.y- self.pose.y, destination_pose.x- self.pose.x) - self.pose.theta)
            self.velocity_publisher.publish(vel_command)
            self.rate.sleep()

        rospy.loginfo("Goal has been reached")
        vel_command.linear.x = 0
        vel_command.angular.z= 0
        self.velocity_publisher.publish(vel_command)

        rospy.spin()
        

if __name__ == '__main__':
    try:
       
        x= autonavigation()
        x.movement()
      
            
    except rospy.ROSInterruptException:
        pass
    
