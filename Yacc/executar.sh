#!/bin/bash

yacc -d scanner.y
lex  scanner.l
gcc -c lex.yy.c y.tab.c
gcc -o parser  lex.yy.o y.tab.o -ll
./parser
