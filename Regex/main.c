#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "regex/regex.h"
//#include <regex.h>

int Executar(char *expressao, char *entrada) {

    int flag = 0;
    if (strcmp(entrada, "") != 0){

        //char *re=(char*)malloc(sizeof(char)*50);
        //strcpy(re,"^([0-9]*[0-9].[0-9]*[0-9])$");
        regex_t reg;
        if (regcomp(&reg, expressao, REG_EXTENDED) == 0){

            if (regexec(&reg, entrada, (size_t)0, 0, 0) == 0){

                flag = 1;
            }
        }
        regfree(&reg);
    }
    return flag;
}
int main(){

    char *entrada = (char *)malloc(sizeof(char) * 50);
    char *expressao = (char *)malloc(sizeof(char) * 50);
    do{

        system("clear");
        printf("Expressão regular: ");
        fflush(stdin);
        fgets(expressao, 50, stdin);
        expressao[strlen(expressao) - 1] = '\0';
        printf("Palavra: ");
        fflush(stdin);
        fgets(entrada, 50, stdin);
        entrada[strlen(entrada) - 1] = '\0';
        if (Executar(expressao, entrada) == 1)
            printf("Entrada aceita!\n\n");

        else

            printf("Entrada não aceita!\n\n");

        getchar();

    } while (strcmp(entrada, "sair") != 0);
    free(expressao);
    free(entrada);

    return 0;
}