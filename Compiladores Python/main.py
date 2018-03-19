import f_posfixa
import testes

infix = input("Digite a expressão infixa\n")
infix = infix.replace(" ", "")

if(f_posfixa.expressao_valida(infix)):
    print(f_posfixa.expressao_perfeita(infix))
    print(f_posfixa.polonesa_reversa(f_posfixa.expressao_perfeita(infix)))
else:
    print("Expressão Inválida\n")

#Essa função possui vários testes feitos para ser analisados, basta descomentar para visualizar
#testes.teste()

