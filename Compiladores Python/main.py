﻿from f_posfixa import Posfixa
from afnd import Automato
from testes import Teste
from afd import AutomatoFinito

'''
Trabalho I de Thiago Silva Pereira e Fernando Noleto
Foi implementado o ponto extra do tratamento dos operadores como simbolo, basta usar \operador
para funcionar espero que não dê bug...
'''
class Main(object):
    def entrada(self, infix):
        pos = Posfixa()
        infix = infix.replace(" ", "")

        if(infix.find('\\') == -1):
            infix = infix.replace('.', '')
            if (pos.expressao_valida(infix)):
                print("\nNa posfixa:")
                print(pos.polonesa_reversa(pos.expressao_perfeita(infix)), "\n")
                return pos.polonesa_reversa(pos.expressao_perfeita(infix))
            else:
                print("Expressão Inválida\n")
                return False
        else:
            if (pos.expressao_valida(infix)):
                print("Na posfixa:")
                print(pos.polonesa_reversa(pos.expressao_perfeita(infix)), "\n")
                return pos.polonesa_reversa(pos.expressao_perfeita(infix))
            else:
                print("Expressão Inválida\n")
                return False

def main():

    #-------------trabalho 1---------------#

    m = Main()
    a = Automato()
    infix = input("Digite a expressão infixa\n")
    if(infix == ""):
        print("Entrada inválida!")
        return

    print('---------------TRABALHO 1----------------')
    

    #-------------trabalho 2---------------#

    #automato finito não determinístico com movimento vazio
    afn = a.gerarAFND(m.entrada(infix))
    
    #-------------trabalho 3---------------#
    af = AutomatoFinito()
    
    #af.transicoes(afn.matrizDeTransicao)
    for i in afn.alfabeto:
        if i == '':
            afn.alfabeto.remove('')

    af.gerarAFD(afn)



if __name__ == "__main__":
    
    main()

    #Essa função possui vários testes feitos para serem analisados, basta descomentar
    #as 2 linhas abaixo para visualizar
    
    #t = Teste()
    #t.teste()










