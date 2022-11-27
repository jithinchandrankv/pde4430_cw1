
#           MOBILE ROBOTICS

##PDE4430_COURSE WORK 1

##Aim

   To move a mobile robot in a meaningful way using the
Robotic Operating System (ROS) , the TurtleSim and perform various task like:

 • Teleoperation using the keyboard, with an option to
change movement speed

•  in the
Turtlesim window

• Avoiding wall collision – Override movement if wall
hitting is imminent

• Vacuum Cleaning behaviour – Covering the entire window
in an efficient manner

• Multiple turtles vacuum cleaning behaviour – 2 is good, 3
or more is great



## Installation

In this course work , created a specific package name pde4430_cw1 inside catkin_ws.Added scripts inside the src file.
Added seperate python file for each task .To run this package,always to run  "roscore" and"rosrun turtlesim turtlesim_node" in the terminal box.




## Task 1 :  Teleoperation using the keyboard

   In this task , turtle will controlled using keyboard keys.Also speed will adjust with help of key.For that , need to run turtlesim_node and teleoperator.py. file in the terminal.
   
   
   ![TELEOPERATOR FIRST](https://user-images.githubusercontent.com/117764288/204133640-c1533317-d4c2-4e63-b903-853f7697c12a.JPG)

   

   while running terminal display the which direction key is pressed.
   
   
   ![TELEOPERATOR RUN](https://user-images.githubusercontent.com/117764288/204133824-833a06f9-ba11-4ba0-a3e9-974ef2b82e82.JPG)
   
   
   
   RQT_GRAPH:It will gives information about subcriber,topics,node ,publisher and flow. 
   
   
   
   
   ![image](https://user-images.githubusercontent.com/117764288/204134098-2b1afbf3-4041-4802-aba2-65fbe8fb00a8.png)


   

   

## Task 2:Autonomous navigation to any given coordinate

In this task , turtle will move to any given position with proper orientation and velocity.For that we need to run  "turtlesim_node " and "turtle_automovement.py " in terminalbox.

After run thE python file in the terminal,terminal will ask for the X and Y destination coordinate.


![image](https://user-images.githubusercontent.com/117764288/204134510-b7a233b2-042e-4745-9986-205b984302d0.png)



If the reached to the given position,it will inform "destination reached".



![automovement move](https://user-images.githubusercontent.com/117764288/204134626-6aef58f3-ba5e-403e-933a-507c82272c51.JPG)



RQT GRAPH:It will gives information about subcriber,topics,node ,publisher and flow.



![rqt automovement](https://user-images.githubusercontent.com/117764288/204134862-982a247f-9dd2-4972-af43-820fa8124b9c.JPG)




## Task 3:Avoiding wall collision

In this task, turtle will detect wall and move away from that.For that assigned the wall limit,incase,it reach to wall,terminal will display like "turtle will hit the wall".



![wall detection](https://user-images.githubusercontent.com/117764288/204141326-c4d99a7d-4f2a-496e-b178-1c5d5afbb989.JPG)



Need to run turtlesim_node,turtle_teleoperator.py and turtle_antiwallcollision.py file in the terminal.


![wall detection move](https://user-images.githubusercontent.com/117764288/204141152-79fedfc7-5188-4855-ade7-d7133d5f58da.JPG)

RQT Graph:It will gives information about subcriber,topics,node ,publisher and flow.

![rqt anticollision](https://user-images.githubusercontent.com/117764288/204141140-0feaa24b-e2c5-472d-9b39-1336349e37b7.JPG)
