import f_posfixa
import testes

'''Trabalho I de Thiago Silva Pereira e Fernando Noleto
Foi implementado o ponto extra do tratamento dos operadores como simbolo, basta usar \operador
para funcionar espero que não dê bug...
'''

infix = input("Digite a expressão infixa\n")
infix = infix.replace(" ", "")

if(infix.find('\\') == -1):
    infix = infix.replace('.', '')
    if (f_posfixa.expressao_valida(infix)):
        print(f_posfixa.polonesa_reversa(f_posfixa.expressao_perfeita(infix)))
    else:
        print("Expressão Inválida\n")
else:
    if (f_posfixa.expressao_valida(infix)):
        print(f_posfixa.polonesa_reversa(f_posfixa.expressao_perfeita(infix)))
    else:
        print("Expressão Inválida\n")

#Essa função possui vários testes feitos para ser analisados, basta descomentar para visualizar
#testes.teste()










