from f_posfixa import Posfixa
import pprint

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
        base.estados.append(0)
        base.estados.append(1)
        base.matrizDeTransicao[(0, simbolo)] = 1
        base.estadoInicial = 0
        base.qtEstadosFinais = 1
        base.estadosFinais.append(0)
        return base

    
    #2 automatos como parâmetro. Automato 1 e Automato 2
    def concatenacao(self, automato1, automato2):
        automato = Automato()
        automato.alfabeto = self.uniao_alfabetos(automato1.alfabeto, automato2.alfabeto)
        automato.qtEstados = automato1.qtEstados + automato2.qtEstados

        automato.estados = automato1.estados.copy()
        for i in range(len(automato2.estados)):
            automato.estados.append(automato1.qtEstados + automato2.estados[i])


        automato.matrizDeTransicao = automato1.matrizDeTransicao.copy()
        for i in automato2.matrizDeTransicao.keys():
            try:
                automato.matrizDeTransicao[(i[0]+automato1.qtEstados, i[1])] = automato2.matrizDeTransicao.get(i) + automato1.qtEstados
            except:
                b = list(automato2.matrizDeTransicao.get(i))
                lista = [x + automato1.qtEstados for x in b]
                automato.matrizDeTransicao[(i[0] + automato1.qtEstados, i[1])] = tuple(lista)
            

        automato.matrizDeTransicao[(automato1.qtEstados-1, '&')] = automato1.qtEstados

        automato.estadoInicial = 0
        automato.estadosFinais = automato.qtEstados-1
        automato.qtEstadosFinais = 1
        
        #print("estado inicial:", automato.estadoInicial)
        #print("estado final:", automato.estadosFinais)

        return automato
    
    #fecho de kleene 
    def fechoDeKleene(self, automato):
        novo_automato = Automato()
        novo_automato.alfabeto = self.uniao_alfabetos([""], automato.alfabeto)

        novo_automato.qtEstados = automato.qtEstados + 2
        # preenchendo os estados do novo automato 
        for i in range(novo_automato.qtEstados):
            novo_automato.estados.append(i)

        # preenchendo as transicoes do automato no automato novo
        for i in automato.matrizDeTransicao.keys():
            try:
                novo_automato.matrizDeTransicao[(i[0] + 1, i[1])] = automato.matrizDeTransicao.get(i) + (novo_automato.qtEstados - automato.qtEstados) - 1
            except :
                b = list(automato.matrizDeTransicao.get(i))
                lista = [x+1 for x in b]
                novo_automato.matrizDeTransicao[(i[0] + 1, i[1])] = tuple(lista)
        
        novo_automato.matrizDeTransicao[(0,'&')] = (1, novo_automato.qtEstados - 1)
        novo_automato.matrizDeTransicao[(automato.qtEstados,'&')] = (novo_automato.qtEstados - automato.qtEstados - 1, novo_automato.qtEstados - 1)


        novo_automato.estadoInicial = 0
        novo_automato.estadosFinais = novo_automato.qtEstados - 1
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
                automato.matrizDeTransicao[(i[0] + 1, i[1])] = automato1.matrizDeTransicao.get(i) + 1
            except TypeError:
                b = list(automato1.matrizDeTransicao.get(i))
                lista = [x+1 for x in b]
                automato.matrizDeTransicao[(i[0] + 1, i[1])] = tuple(lista)
        
        
        for i in automato2.matrizDeTransicao.keys():
            try: 
                automato.matrizDeTransicao[(i[0] + automato1.qtEstados + 1, i[1])] = automato2.matrizDeTransicao.get(i) + automato1.qtEstados + 1
            except TypeError:
                b = list(automato2.matrizDeTransicao.get(i))
                lista = [x + automato1.qtEstados + 1 for x in b]
                automato.matrizDeTransicao[(i[0] + automato1.qtEstados + 1, i[1])] = tuple(lista)
        
        
        if ((automato1.qtEstados, '&')) in automato.matrizDeTransicao.keys():
            automato.matrizDeTransicao[(automato1.qtEstados, '&')] = automato1.matrizDeTransicao.get((automato1.qtEstados, '&')), automato.qtEstados - 1
        else:
            automato.matrizDeTransicao[(automato1.qtEstados,'&')] = automato.qtEstados - 1
        
        
        if (automato2.qtEstados + automato1.qtEstados, '&') in automato.matrizDeTransicao.keys():
            automato.matrizDeTransicao[(automato2.qtEstados + automato1.qtEstados, '&')] = automato2.matrizDeTransicao.get((automato2.qtEstados + automato1.qtEstados, '&')), automato.qtEstados - 1
        else:
            automato.matrizDeTransicao[(automato2.qtEstados + automato1.qtEstados,'&')] = automato.qtEstados - 1
        

        automato.estadoInicial = 0
        automato.estadosFinais = automato.qtEstados - 1
        automato.qtEstadosFinais = 1
        
        return automato

    '''
    #Função de gerenciamento do automato dado a entrada da posfixa
    def gerarAFND(self, posfixa):
        for i in range(len(posfixa)):
            simbolo = posfixa[i]
            if self.ehOperando(simbolo):
                self.pilhaAutomato.append(self.base(simbolo))
            else:
                if self.pilhaAutomato:
                    if simbolo == '*':
                        self.pilhaAutomato.append(self.fechoDeKleene(self.pilhaAutomato.pop()))
                    elif self.pilhaAutomato:
                        op2 = self.pilhaAutomato.pop()
                        op1 = self.pilhaAutomato.pop()
                        if simbolo == "+":                         
                            self.pilhaAutomato.append(self.uniao(op1,op2))
                        elif simbolo == '.':
                            self.pilhaAutomato.append(self.concatenacao(op1,op2))
        
        afn = self.pilhaAutomato.pop()
        afn.matrizDeTransicao[(len(afn.matrizDeTransicao), ' ')] = ' '
        
        pprint.pprint(afn.matrizDeTransicao)
        print("\nEstado Inicial: ", afn.estadoInicial)
        print("Estado Final: ", afn.estadosFinais, "\n")
        if not self.pilhaAutomato:
            pprint.pprint(afn)
        return afn.matrizDeTransicao
    '''

    #Função de gerenciamento do automato dado a entrada da posfixa
    def gerarAFND(self, posfixa):
        for i in range(len(posfixa)):
            simbolo = posfixa[i]
            if self.ehOperando(simbolo):
                self.pilhaAutomato.append(self.base(simbolo))
            else:
                if self.pilhaAutomato:
                    if simbolo == '*':
                        self.pilhaAutomato.append(self.fechoDeKleene(self.pilhaAutomato.pop()))
                    elif self.pilhaAutomato:
                        op2 = self.pilhaAutomato.pop()
                        op1 = self.pilhaAutomato.pop()
                        if simbolo == "+":                         
                            self.pilhaAutomato.append(self.uniao(op1,op2))
                        elif simbolo == '.':
                            self.pilhaAutomato.append(self.concatenacao(op1,op2))
        
        afn = self.pilhaAutomato.pop()
        afn.matrizDeTransicao[(len(afn.matrizDeTransicao), ' ')] = ' '
        
        print('---------------TRABALHO 2----------------')
        
        pprint.pprint(afn.matrizDeTransicao)
        print("\nEstado Inicial: ", afn.estadoInicial)
        print("Estado Final: ", afn.estadosFinais, "\n")
        if not self.pilhaAutomato:
            pprint.pprint(afn)
        return afn



if __name__ == "__main__":
    pass
    #automato = Automato()
    #entrada = main.entrada()
    #if (entrada == False):
    #    print("Entrada inválida")
    #else:
    #    automato.gerarAFND(entrada)