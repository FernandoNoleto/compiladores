import f_posfixa
import main

class Automato(object):
 
    def __init__(self):
        self.alfabeto = []
        self.estados = []
        self.qtEstados = 0
        self.matrizDeTransicao = {}
        self.estadoInicial = 0
        self.estadosFinais = []
        self.qtEstadosFinais = 0   


    def base(self, simbolo):
        base = Automato()
        base.alfabeto.append(simbolo)
        base.qtEstados = 2
        base.estados = [base.qtEstados]
        base.estados.append(0)
        base.estados.append(1)
        base.matrizDeTransicao[(0, simbolo)] = 1
        base.estadoInicial = 0
        base.qtEstadosFinais = 1
        base.estadosFinais.append(0)
        return base
    
    def uniao_alfabetos(self, alfabeto1, alfabeto2):
        novo_alfabeto = alfabeto1.copy()
        for i in range(len(alfabeto2)):
            if not alfabeto2[i] in alfabeto1:
                novo_alfabeto.append(alfabeto2[i])
        return novo_alfabeto

    #2 automatos como parâmetro. Automato 1 e Automato 2
    def concatenacao(self, automato1, automato2):
        novo = Automato()
        novo.alfabeto = self.uniao_alfabetos(automato1.alfabeto, automato2.alfabeto)
        novo.qtEstados = automato1.qtEstados + automato2.qtEstados

        novo.estados = automato1.estados.copy()
        for i in range(len(automato2.estados)):
            novo.estados.append( automato1.qtd_estados + automato2.estados[i])


        novo.matrizDeTransicao = automato1.matrizDeTransicao.copy()
        for i in automato2.matrizDeTransicao.keys():
            try:
                novo.matrizDeTransicao[ (i[0]+automato1.qtdEstados, i[1] ) ] = automato2.matrizDeTransicao.get(i) + automato1.qtdEstados
            except :
                b = list(automato2.matrizDeTransicao.get(i))
                lista = [x+automato1.qtdEstados for x in b]
                novo.matrizDeTransicao[ (i[0]+automato1.qtdEstados, i[1] ) ] = tuple(lista)
            

        novo.matrizDeTransicao[(automato1.qtdEstados-1, '&')] = automato1.qtdEstados

        novo.estadoInicial = 0
        novo.estadoFinal = novo.qtEstados-1
        novo.qtEstadosFinais = 1
        
        print("estado inicial:", novo.estadoInicial)
        print("estado final:", novo.estadosFinais)

        return novo
    
    def gerarAFND(self):
        pass


if __name__ == "__main__":
    automato = Automato()
    entrada = main.entrada()
    if (entrada == False):
        print("Entrada inválida")
    else:
        automato.gerarAFND()
