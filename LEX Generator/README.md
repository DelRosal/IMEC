Deliverable II: Lex Generator
=============

INTRODUCTION

### Logic ###


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


## Sentences ##

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

## Links ##

__**[Github Main Project link](https://github.com/DelRosal/IMEC "Main Project")**__

__**[Github Deliverable I link](https://github.com/DelRosal/IMEC/tree/main/LEX%20Generator "Deliverable II")**__ 
