# 2022 SINICA Project - Control TM robot arm by joystick

### The purpose of this project is to read the joint angle of joystick and send the angle values to TM robot arm, which can make the trajectory of joystick and robot arm be the same. Also, We create a user interface to let user easier to use and to modify the parameters of the program. ###
---
Here are three parts:
+ [read_joystick.py](./read_joystick.py)
+ [move_robot.py](./move_robot.py)
+ [joystick_ui.py](./joystick_ui.py)

### (a) read_joystick.py ###
> In this program, users need to connect the computer and the joystick (or PCB) by uart protocol, and to change the COM to 10 (PCB for test) or 20 (joystick). Besides, users should modify the commands and serial port setting, and the program will return the angle values to the UI. If users use the PCB to test, please import [read_joystick_test.py](./read_joystick_test.py) in [joystick_ui.py](./joystick_ui.py).

### (b) move_robot.py ###
> Before running the program, users should modify the IP address as the TM robot arm's (using 127.0.0.1 and running [server.py](./server.py) for testing). Because this program is only for "TM Robot Arm" to "Move Point to Point", if users want to do more tasks, the commands of TM robot arm should be modified correspondingly.

### (c) joystick_ui.py ###
> After finishing modifying above programs, users can run this program directly. Users should connect the joystick, return the joint angle values to zero, and input (or import) initial values; then, when users connect the robot arm, the robot arm will move along the same path as the jotstick. Moreover, users can save the initial setting as a json file, and import them next time.
---
### _Note: Please plug all devices before running the program, and do NOT change the initial value when running._ ###
#### _This version hasn't been finished. If you have any problem, please contact b08502148@ntu.edu.tw._ ####