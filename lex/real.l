%{
    #include  <stdio.h>
%}

%%

    /*  Regra  usada  para  encontrar  algum  numero  real  */

([0 -9]*\.) *[0 -9]+    {
    printf("Real: %s\n", yytext);
    }
    
.   {
        /*  Ignora  outros  caracteres. */
    }

%%

/***  secao  de  codigo C ***/

int  main(void) {
    /*  executa o analisador  lexico. */
    yylex ();
    return  0;
}