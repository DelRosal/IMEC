%{
#include "y.tab.h"
extern int yylval;
%}

%%

Robot|robot                             { return ROBOT; }
you                                   { return NOUN; }
could                               { return REQUEST; }
Please|please                                  { return PLEASE; }
move                                    { return MOVE; }
turn                                    { return TURN; }
ahead                                   { return DIRECTION; }
blocks|blocks,                          { return BLOCKS; }
degrees|degrees,                        { return DEGREEW; }
and|then                                { return CONJUNTION; }
forward|left|right|top|bottom|backwards { return DIRECTION; }
90|180|270|360                          { yylval = atoi(yytext); return DEGREES; }
[0-9]+                                  { yylval = atoi(yytext); return AMOUNT; }

[ \t] ; 			/* ignore whitespace */
\n                  {return 0;} 		
.                   return yytext[0];
