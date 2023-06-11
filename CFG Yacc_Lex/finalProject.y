%{
#include <stdlib.h>
#include <stdio.h>
#include <string.h>

int yylex();
char *inst[10];
int count = 0;
void yyerror(const char *s);
extern FILE *yyin;
%}

%token AMOUNT DIRECTION DEGREES ROBOT PLEASE MOVE TURN BLOCKS CONJUNTION DEGREEW NOUN REQUEST
%%

sentence: sentences { printf("PASS\n"); };

sentences: ROBOT PLEASE instructions
        | ROBOT instructions PLEASE   
        | PLEASE instructions     
        | ROBOT question instructions PLEASE '?'     
        | ROBOT question PLEASE instructions '?'
        ;  

question:  REQUEST NOUN
        ;

instructions: instruction 
            | instructions CONJUNTION instruction
            | instructions CONJUNTION CONJUNTION instruction
            ;

instruction: MOVE AMOUNT BLOCKS {
                int value = $2;
                int size = snprintf(NULL, 0, "MOV,%d", value); 
                char* formattedString = malloc(size + 1);
                snprintf(formattedString, size + 1, "MOV,%d", value);
                inst[count] = malloc(strlen(formattedString) + 1);
                strcpy(inst[count], formattedString);
                count++;
            }
            | MOVE AMOUNT BLOCKS DIRECTION {
                int value = $2;
                int size = snprintf(NULL, 0, "MOV,%d", value); 
                char* formattedString = malloc(size + 1);
                snprintf(formattedString, size + 1, "MOV,%d", value);
                inst[count] = malloc(strlen(formattedString) + 1);
                strcpy(inst[count], formattedString);
                count++;
            }
            | TURN DEGREES DEGREEW{
                int value = $2;
                int size = snprintf(NULL, 0, "TURN,%d", value); 
                char* formattedString = malloc(size + 1);
                snprintf(formattedString, size + 1, "TURN,%d", value);
                inst[count] = malloc(strlen(formattedString) + 1);
                strcpy(inst[count], formattedString);
                count++;
            }
            ;

%%

void yyerror(const char *s){
    printf("FAIL\n");
}

int main(int argc, char **argv){
    if(argc != 2){
        fprintf(stderr, "Usage: %s <input_file>\n", argv[0]);
        exit(1);
    }

    FILE *input = fopen(argv[1], "r");
    if(!input){
        perror("fopen");
        exit(1);
    }
    yyin = input;
    yyparse();
    fclose(input);

    FILE *fp;
    fp = fopen("instructions.asm","w");
    
    for (int i = 0; i < count; i++) {
        if (inst[i] == NULL) return 0;
        fprintf(fp,"%s\n",inst[i]);
    }

    return 0;
}
