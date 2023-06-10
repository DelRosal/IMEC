Deliverable I: Basic CPU
=============

In the last century, efficiency has become  a crucial concept in the manufacturing field; automatization is everywhere, with an increasing need for specialized equipment. That’s where robots come in.

Programming and designing a machine capable of realizing tasks previously made by humans can both decrease manufacture time and increase product quality. Therefore, our mission is to design a compiler capable of processing human instructions, convert them into code that is understandable for the robot, and finally implement the necessary logic for the robot to execute its duty.

To generate a compiler we need to implement different files that interact with each other simplifying human instructions.


<img width="800" alt="Picture1" src="https://github.com/DelRosal/IMEC/assets/99361062/55a61119-4c3f-46bd-936e-9c12cc7dab59">


First, it is required to define the robot’s characteristics and limitations as it is shown in the following list:

1. The robot is capable of moving only **forward** 
2. The robot is capable of **rotation** (90,180,270,360)
3. The robot only understands the following commands:
    1. **MOV  X** (where X represents any integer) 
    2. **TURN** (90,180,270,360)
4. The robot operates inside a **10 x 10**  matrix 
5. The robot only follows **polite** instructions

![Picture3](https://github.com/DelRosal/IMEC/assets/99361062/61e2e567-650d-4494-83b3-cbdf4eb0f064)

After reviewing the specifications, we were able to generate a ***fine automata***, which dictates the rules and input for the robot.

### Machine States ###

Fine Automata| Rules  
------------- | -------------
States                      𝑸  | WAITING,  ←, ↑, →, ↓, PIT STOP, MOVE
Alphabet                    ∑  | MOV X, TURN (90,180,270,360), EMPTY
Transition function            | Shown in diagram and table
Start State            q - >𝑸  | WAITING
Accept State           F -> 𝑸  | WAITING

<img width="800" alt="Picture2" src="https://github.com/DelRosal/IMEC/assets/99361062/4a1c4a31-ac7c-4373-b0b0-cb20ef66dc41">

### Transition function ###
STATES        | MOV X         | TURN 90       | TURN 180      | TURN 270      | TURN 360      | EMPTY
------------- | ------------- | ------------- | ------------- | ------------- | ------------- | -------------
WAITING       | MOVE          | ↑             | ←             | ↓             | →             | -
←             | -| - | - | -  | - | PIT STOP
↑             | - | -  | - | -| -| PIT STOP
→             | - | - | - | - | - | PIT STOP
↓             |- | -  | - | -  | - | PIT STOP
PIT STOP      | - | -  | -| - | - | WAITING
MOVE          | - | -  | -| - | - | WAITING

Each state represents a function that the python file executes, with the exception of “WAITING” and “PIT STOP” which are intermediate states between instructions. Consequently, WAITING is the starting and accepting state.

On the other hand, the alphabet is a set of triggers (instructions) that initiate different functions. For example, if the robot is in the WAITING state and receives “MOV 3” it will provoke the MOVE function to start (with 3 as an argument), and then return to the WAITING state.


__**[Github Main Project link](https://github.com/DelRosal/IMEC "Main Project")**__

__**[Github Deliverable I link](https://github.com/DelRosal/IMEC/tree/main/Basic%20CPU "Deliverable I")**__ 
