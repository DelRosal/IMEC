#!/bin/bash
input="./unitTest.txt"
is_pass=1

echo " "
echo "CPU automaton for basic robot | Unit Test"
echo " "
echo "Santiago Vera Espinoza | A01641585"
echo "Ana Luisa G. Del Rosal | A01566927 "
echo "Iker Ochoa Villaseñor  | A0164098"

yacc -d finalProject.y
lex finalProject.l
gcc y.tab.c lex.yy.c -ly -ll -o finalProject

sleep 2
clear
while IFS= read -r line
do
    if [ -z "$line" ]; then
        is_pass=0
        continue
    fi

    echo "Instruction:"
    echo "$line"
    echo "Expected answer:"

    if [ $is_pass -eq 1 ] ; then
        echo 'PASS'
        echo ''
        echo "Executing compiler..."
        sleep 3
        echo ''
        echo 'Answer: '
        echo "$line" > instructions.txt
        ./finalProject instructions.txt
        echo "Executing python..."
        sleep 2
        python3 cpu.py
        sleep 3

        else 
        echo 'FAIL'
        echo ''
        echo "Executing compiler..."
        sleep 3
        echo ''
        echo 'Answer: '
        echo "$line" > instructions.txt
        ./finalProject instructions.txt
        echo "Jumping Next Instruction..."
        sleep 4
    fi
    clear
done < "$input"
