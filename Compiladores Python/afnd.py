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
        self.pilhaAutomato = [Automato]

    #É operando?
    def ehOperando(self, simbolo):
        if (simbolo != '+' and simbolo != '-' and simbolo !=  '/' and simbolo  != '(' and simbolo != ')' and simbolo != '*' and simbolo != '.'):
            return True
        else:
            return False

    #União de alfabetos
    def uniao_alfabetos(self, alfabeto1, alfabeto2):
        novo_alfabeto = alfabeto1.copy()
        for i in range(len(alfabeto2)):
            if not alfabeto2[i] in alfabeto1:
                novo_alfabeto.append(alfabeto2[i])
        return novo_alfabeto


    #Quando entra algum símbolo
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

    
    #2 automatos como parâmetro. Automato 1 e Automato 2
    def concatenacao(self, automato1, automato2):
        novo = Automato()
        novo.alfabeto = self.uniao_alfabetos(automato1.alfabeto, automato2.alfabeto)
        novo.qtEstados = automato1.qtEstados + automato2.qtEstados

        novo.estados = automato1.estados.copy()
        for i in range(len(automato2.estados)):
            novo.estados.append(automato1.qtEstados + automato2.estados[i])


        novo.matrizDeTransicao = automato1.matrizDeTransicao.copy()
        for i in automato2.matrizDeTransicao.keys():
            try:
                novo.matrizDeTransicao[ (i[0]+automato1.qtEstados, i[1] ) ] = automato2.matrizDeTransicao.get(i) + automato1.qtEstados
            except :
                b = list(automato2.matrizDeTransicao.get(i))
                lista = [x+automato1.qtEstados for x in b]
                novo.matrizDeTransicao[ (i[0]+automato1.qtEstados, i[1] ) ] = tuple(lista)
            

        novo.matrizDeTransicao[(automato1.qtEstados-1, '&')] = automato1.qtEstados

        novo.estadoInicial = 0
        novo.estadoFinal = novo.qtEstados-1
        novo.qtEstadosFinais = 1
        
        print("estado inicial:", novo.estadoInicial)
        print("estado final:", novo.estadosFinais)

        return novo
    
    #fecho de kleene 
    def fechoDeKleene(self, automato):
        novo_automato = Automato()
        novo_automato.alfabeto = self.uniao_alfabetos([""], automato.alfabeto)

        novo_automato.qtd_estados = automato.qtEstados + 2
        # preenchendo os estados do novo automato 
        for i in range(len(automato.estados)):
            novo_automato.estados.append(i)

        # preenchendo as transicoes do automato1 no automato novo
        for i in automato.matrizDeTransicao.keys():
            try:
                novo_automato.matrizDeTransicao[ (i[0]+1, i[1] ) ] = automato.matrizDeTransicao.get(i) + (novo_automato.qtEstados - automato.qtEstados) - 1
            except :
                print(i)
                b = list(automato.matrizDeTransicao.get(i))
                print(b)
                print("automato com lista de transicoes")
                lista = [x+1 for x in b]
                print('transicoes ',lista)
                novo_automato.matrizDeTransicao[ (i[0]+1, i[1] ) ] = tuple(lista)
                print( novo_automato.matrizDeTransicao[ (i[0]+1, i[1] ) ] )
        
        novo_automato.matrizDeTransicao[(0,'&')] = (1,novo_automato.qtEstados-1)
        novo_automato.matrizDeTransicao[(automato.qtEstados,'&')] = (novo_automato.qtEstados - automato.qtEstados -1, novo_automato.qtEstados-1)



        novo_automato.estadoInicial = 0
        novo_automato.estadosFinais = novo_automato.qtEstados-1
        novo_automato.qtEstadosFinais = 1
         
        return novo_automato

    #União entre 2 automatos
    def uniao(self, automato1, automato2):
        automato = Automato()
        automato.alfabeto = self.uniao_alfabetos(automato1.alfabeto, automato2.alfabeto)
        automato.qtEstados = automato1.qtEstados + automato2.qtEstados + 2

        for i in range(automato.qtEstados):
            automato.estados.append(i)
        
        automato.matrizDeTransicao[(0, '&')] = automato1.estadoInicial + 1, automato2.estadoInicial + automato1.qtEstados + 1

        for i in automato1.matrizDeTransicao.keys():
            try:
                automato.matrizDeTransicao[(i[0]+1, i[1])] = automato1.matrizDeTransicao.get(i) + 1
                print(automato.matrizDeTransicao)
            except TypeError :
                print(automato1.matrizDeTransicao.get(i))
                b = list(automato1.matrizDeTransicao.get(i))
                lista = [x+1 for x in b]
                automato.matrizDeTransicao[ (i[0]+1, i[1] ) ] = tuple(lista)
        print("Transicao 1", automato.matrizDeTransicao)
        
        
        for i in automato2.matrizDeTransicao.keys():
            try: 
                automato.matrizDeTransicao[ (i[0]+automato1.qtEstados + 1, i[1] ) ] = automato2.matrizDeTransicao.get(i) + automato1.qtEstados + 1
            except TypeError :
                b = list(automato2.matrizDeTransicao.get(i))
                lista = [x+automato1.qtEstados + 1 for x in b]
                automato.matrizDeTransicao[ (i[0]+automato1.qtEstados + 1, i[1] ) ] = tuple(lista)
        print("Transicao 2", automato.matrizDeTransicao)
        
        
        print (automato1.qtEstados)
        if ((automato1.qtEstados, '&')) in automato.matrizDeTransicao.keys():
            automato.matrizDeTransicao[(automato1.qtEstados,'&')] = automato1.matrizDeTransicao.get((automato1.qtEstados, '&')), automato.qtEstados-1
        else:
            automato.matrizDeTransicao[(automato1.qtEstados,'&')] = automato.qtEstados-1
        print("Transicao if 1", automato.matrizDeTransicao)
        
        
        print (automato2.qtEstados+automato1.qtEstados)
        if (automato2.qtEstados+automato1.qtEstados, '&') in automato.matrizDeTransicao.keys():
            automato.matrizDeTransicao[( automato2.qtd_estado+automato1.qtEstados,'&')] = automato2.matrizDeTransicao.get((automato2.qtEstados+automato1.qtEstados, '&')), automata.qtEstados-1
        else:
            automato.matrizDeTransicao[(automato2.qtEstados + automato1.qtEstados,'&')] = automato.qtEstados-1
        print("Transicao if 2", automato.matrizDeTransicao)

        automato.estado_inicial = 0
        automato.estado_final = automato.qtEstados-1
        automato.qtd_estado_final = 1
        
        return automato

    
    #Função de gerenciamento do automato dado a entrada da posfixa
    def gerarAFND(self, posfixa):
        for i in range(len(posfixa)):
            simbolo = posfixa[i]
            if self.ehOperando(simbolo):
                self.pilhaAutomato.append(self.base(simbolo))
            else:
                if self.pilhaAutomato:
                    if simbolo == '*':
                        self.pilhaAutomato.append(self.fechoDeKleene(self.pilhaAutomato.pop()) )
                    elif self.pilhaAutomato :
                        op2 = self.pilhaAutomato.pop()
                        op1 = self.pilhaAutomato.pop()
                        if simbolo == "+":
                            print("Uniao")
                            self.pilhaAutomato.append(self.uniao(op1,op2) )
                        elif simbolo == '.':
                            print("Concatenacao")
                            self.pilhaAutomato.append(self.concatenacao(op1,op2) )
        
        afn = self.pilhaAutomato.pop()
        print(afn.matrizDeTransicao)
        if not self.pilhaAutomato:
            print(afn)
        return afn.matrizDeTransicao


if __name__ == "__main__":
    automato = Automato()
    entrada = main.entrada()
    if (entrada == False):
        print("Entrada inválida")
    else:
        automato.gerarAFND(entrada)