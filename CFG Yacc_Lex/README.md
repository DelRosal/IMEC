Deliverable III: CGF with Lex and Yacc
=====

After generating the tokens that simplify human language, a Context Free Grammar is needed to finish processing the instruction. The CFG will combine different tokens to form new variables that can compose a final variable that is accepted by the compiler and CPU. This way, different phrasing can lead to the same result. 

Taking under consideration that the robot can only accomplish the instructions:

1. MOV X (X being an integer)
2. TURN Y (Y being 90,180,270,360)

The following CFG was generated.

### Context Free Grammar ###
<img width="650" alt="image" src="https://github.com/DelRosal/IMEC/assets/99361062/55dc64b4-8795-46f7-b55f-bc2f0bca8fbb">

The Yacc is composed by the different variables available, and then it tries to form a sentence (final variable). If the program suceeds, it can then translate the sentence into the Robots language, if not, it will show an error as the input was not valid.


### Inputs ###

The following lists show both VALID and INVALID inputs: 

#### Valid Sentences ####
1. Robot please move 2 blocks ahead
2. Robot please move 2 blocks 
3. Robot please move 3 blocks ahead and the turn 90 degrees, and then move 2 blocks
4. Robot please turn 270 degrees and then move 2 blocks
5. Robot could you please move 3 blocks?
6. Robot could you move 3 blocks please?
7. Robot move 3 blocks please
8. Please move 3 blocks

#### Invalid Sentences ####
1. Robot please move 2 
2. Robot please turn 90
3. Robot move 3 blocks  
4. Move 2 blocks and then turn 90 degrees
5. Robot move 5 ahead and turn 360 degrees
6. Robot please turn 20 degrees 
7. Turn 90 degrees and then move 3 blocks
8. move 4 blocks

### Example ###

<img width="650" alt="image" src="https://github.com/DelRosal/IMEC/assets/99361062/22cf1f47-8d4a-49e0-bc5d-ac10de972d21">



PROGRESS      | INSTRUCTION
------------- | -------------
Human language| Robot please move 3 blocks ahead and then turn 90 degrees, and then move 2 blocks
Lex           | ROBOT PLEASE MOVE AMOUNT BLOCKS DIRECTION CONJUNCTION CONJUNCTION TURN DEGREES DEGREEW CONJUNCTION CONJUNCTION MOVE AMOUNT BLOCKS
Yacc          | MOV 3, TURN 90, MOV 2


## Links ##

__**[Github Main Project link](https://github.com/DelRosal/IMEC "Main Project")**__

__**[Github Deliverable III link](https://github.com/DelRosal/IMEC/tree/main/CFG%20Yacc_Lex "Deliverable III")**__ 
