
#           MOBILE ROBOTICS

PDE4430_COURSE WORK 1

Aim

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

   

## Task 2:Autonomous navigation to any given coordinate

In this task , turtle will move to any given position with proper orientation and velocity.For that we need to run  "turtlesim_node " and "turtle_automovement.py " in terminalbox.

After run thE python file in the terminal,terminal will ask for the X and Y destination coordinate.If the reached to the given position,it will inform "destination reached". 

## Task 3:Avoiding wall collision

In this task, turtle will detect wall and move away from that.For that assigned the wall limit,incase,it reach to wall,terminal will display like "turtle will hit the wall".
Need to run turtlesim_node and turtle_antiwallcollision.py file in the terminal.
