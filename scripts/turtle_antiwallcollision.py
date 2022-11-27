#!/usr/bin/env python3
# license removed for brevity

import rospy
import getch
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
import math

move_cmd = Twist()
pub = rospy.Publisher ('turtle1/cmd_vel', Twist, queue_size=10)

#Rotate180 function rotate the turtle when it reaches to limit
def rotate180():

    t0 = rospy.Time.now().to_sec()
    currentAngle=0
    move_cmd.angular.z= 3
    move_cmd.linear.x = 1
    rotate= math.radians(180)

    while currentAngle<3.14/180:

        print("CurrentAngle : ",currentAngle)
        t1 = rospy.Time.now().to_sec()
        currentAngle = move_cmd.angular.z * (t1-t0)
        pub.publish(move_cmd)

    move_cmd.linear.x = 0
    move_cmd.angular.z = 0
    pub.publish(move_cmd)

    
#This function checks wall detection
def callback (data):
    
    if ((data.x <= 0.5 or data.y >=10.2)):
        rotate180()
        rospy. loginfo("turtle hit the wall")
        

    elif (( data.x >=10.2 or data.y <= 0.7)):
        rotate180()
        rospy. loginfo("turtle hit the wall")

    elif (data.x == 0.5 and data.y == 0.7):
        rotate180()
        rospy. loginfo("turtle hit the wall")

    elif (data.x >= 10.2 and data.y >= 10.2):
        rotate180()
        rospy. loginfo("turtle hit the wall")

#walldetect function ,it subscribes pose and publish twist

def walldetect():

    rospy. init_node('turtle_antiwallcollision', anonymous=True)

    rospy.Subscriber("/turtle1/pose", Pose , callback)

    pub = rospy.Publisher ('turtle1/cmd_vel', Twist, queue_size=10)
    
    rospy.spin()

#main function calls walldetect()
if __name__ == '__main__' :
    try:
        walldetect()
    except rospy.ROSInterruptException:
        pass