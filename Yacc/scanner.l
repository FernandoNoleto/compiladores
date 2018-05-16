%{
#include <stdlib.h>
void yyerror(char *);
#include "y.tab.h"
%}

%%
[0-9]+ {
    yylval = atoi(yytext);
    return INTEGER;
}

[-+*/\n] return *yytext;

[ \t] ; /* ignorar espaços em branco */

. yyerror("caracter invalido");

%%
int yywrap(void) {
    return 1;
}