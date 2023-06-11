Implementation of Computational Methods: Robot Language Compiler
=====

Tecnológico de Monterrey Campus Guadalajara

Victor Rodríguez


## Students ##
Ana Luisa G. del Rosal A01566927

Iker Ochoa Villaseñor  A01640984

Santiago Vera Espinoza A01641585

## Deliverable I: Basic CPU ##


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

### CPU Simulator ###

The CPU Simulator in Python works using a coordenates class. This object has overloaded operators that manage the operations with the different coordenates, and the corresponding limits of the matrix. The class uses an integer to determine the Robot's direction, and depending on its value, a different directional coordenate is chosen.

The script reads the instructions and split them by the commas (,). That way the CPU Simulator can determine the action it must do as well as the quantity of times. Each movement is generated and presented in a map with UNICODE characters, representing the current values, direction and position of the robot. If the script recieves a MOVE instruction that exceeds the matrix, the robot will remain in its last position.

__**[Github Deliverable I link](https://github.com/DelRosal/IMEC/tree/main/Basic%20CPU "Deliverable I")**__ 

## Deliverable II: Lex Generator ##

This segment of the project is in charge of generating tokens that simplify common human instructions, so they can be later processed and traduced for the CPU Simulator. To generate the tokens it must be considered the different ways a human can generate a command with the same outcome. 

### Logic ###

The robot is only capable of understand MOVE and TURN directions, therefore, an alalysis was made upon each instruction, its components and the diverse phrasings. 

The following list shows the parts of a human instruction:

1. **Parts of a sentence**
    1. Noun: The robot is addressed in the sentence as a being or its name.
    2. Politeness: Every instruction must be polite, including a please.
    3. Structure: The instruction can be phrased as a command or a question.
    
3. **Instruction MOVE**
    1. Movement action: Key word that asks specifically for movement
    2. Quantity: The quantity of spaces thar the robot should move
    3. Type of quanity: Blocks
    4. Movement Direction: Forward
    
5. **Instruction TURN**
    1. Turn action: Key word that asks specifically for a turn
    2. Quantity: 90, 180, 270, 360
    3. Type of quantity: Degrees
  

From the results, the follwing tokens were generated.


### Tokens ###
TOKEN         | DEFINITION
------------- | -------------
ROBOT         | Robot \| robot
NOUN          | you
REQUEST       | Could
PLEASE        | please
MOVE          | move
TURN          | turn
DIRECTION     | ahead
BLOCKS        | block \| blocks,
DEGREEW       | degrees \| degrees,
CONJUNCTION   | and \| then
DIRECTION     | forward \| left \| right \| top \| bottom \| backwards
DEGREES       | 90 \| 180 \| 270 \| 360
AMOUNT        | [0-9]+


### Sentences ###

### Valid Sentences ###
1. Robot please move 2 blocks ahead
2. Robot please move 2 blocks 
3. Robot please move 3 blocks ahead and the turn 90 degrees, and then move 2 blocks
4. Robot please turn 270 degrees and then move 2 blocks
5. Robot could you please move 3 blocks?
6. Robot could you move 3 blocks please?
7. Robot move 3 blocks please
8. Please move 3 blocks

### Invalid Sentences ###
1. Robot please move 2 
2. Robot please turn 90
3. Robot move 3 blocks  
4. Move 2 blocks and then turn 90 degrees
5. Robot move 5 ahead and turn 360 degrees
6. Robot please turn 20 degrees 
7. Turn 90 degrees and then move 3 blocks
8. move 4 blocks

__**[Github Deliverable II link](https://github.com/DelRosal/IMEC/tree/main/LEX%20Generator "Deliverable II")**__ 

## Deliverable III: CGF with Lex and Yacc ##

After generating the tokens that simplify human language, a Context Free Grammar is needed to finish processing the instruction. The CFG will combine different tokens to form new variables that can compose a final variable that is accepted by the compiler and CPU. This way, different phrasing can lead to the same result. 

Taking under consideration that the robot can only accomplish the instructions:

1. MOV X (X being an integer)
2. TURN Y (Y being 90,180,270,360)

The following CFG was generated.

### Context Free Grammar ###
<img width="650" alt="image" src="https://github.com/DelRosal/IMEC/assets/99361062/55dc64b4-8795-46f7-b55f-bc2f0bca8fbb">

The Yacc is composed by the different variables available, and then it tries to form a sentence (final variable). If the program suceeds, it can then translate the sentence into the Robots language, if not, it will show an error as the input was not valid.


### Example ###

<img width="650" alt="image" src="https://github.com/DelRosal/IMEC/assets/99361062/22cf1f47-8d4a-49e0-bc5d-ac10de972d21">


PROGRESS      | INSTRUCTION
------------- | -------------
Human language| Robot please move 3 blocks ahead and then turn 90 degrees, and then move 2 blocks
Lex           | ROBOT PLEASE MOVE AMOUNT BLOCKS DIRECTION CONJUNCTION CONJUNCTION TURN DEGREES DEGREEW CONJUNCTION CONJUNCTION MOVE AMOUNT BLOCKS
Yacc          | MOV 3, TURN 90, MOV 2


__**[Github Deliverable III link](https://github.com/DelRosal/IMEC/tree/main/CFG%20Yacc_Lex "Deliverable III")**__ 

## Deliverable IV: Scripting and Unit Testing ##

The unit test runs in a Bash Script making it possible to execute all files at once. Inside a text file, the test cases are divided between successful and failing tests.

A Bash Script opens the text file and through a while loop, each line of text is read and individually the following scripts are executed:

1. The line that is currently being read is written to the instructions.txt file, becoming the input of the compiler and dictating the possible results.
2. The finalProyect.exec file is executed, which contains the yacc and lex libraries that create the parser, which will check if the input is valid, as well as generate the instructions.asm file, containting the instructions that the CPU will recieve. The result must PASS, otherwise it will FAIL and stop the process.
3. In the input is valid,  the python CPU Simulation is excecuted, having the .asm as input and showing in real time the movements made by the robot and its destination.

The cycle is repeated until all the text lines of the test cases are analyzed.

__**[Github Deliverable IV link](https://github.com/DelRosal/IMEC/tree/main/Final%20Delivery "Deliverable IV")**__ 


## Running the Robot Language Compiler ##

After downloading the repository, run the following command:

<img width="700" alt="image" src="https://github.com/DelRosal/IMEC/assets/99361062/20abeeea-143f-4f10-ace3-007d02c44320">

## Appendix ##

<img width= "700" alt="image" src="https://github.com/DelRosal/IMEC/assets/99361062/2b247082-814d-403b-9002-2db5d1e56725">

<img width= "700" alt="image" src="https://github.com/DelRosal/IMEC/assets/99361062/484304c3-31e7-41d2-b9ba-66f1fa0dea55">

