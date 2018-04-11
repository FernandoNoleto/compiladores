from afnd import Automato

class AutomatoFinito(Automato):
    
    def __init__(self):
        super().__init__()

    #Matriz de transição e automato->int
    def fechoE(self, matrizDeTransicao, automato):
        lista = []
        lista.append(automato)
        
        for i in matrizDeTransicao:
            if(i[0] == automato and i[1] == "&"):    
                aux = matrizDeTransicao.get(i)
                if type(aux) == int:
                    lista.append(aux)
                else:
                    for a in aux:
                        lista.append(a)
        
        for i in lista:
            for j in matrizDeTransicao:
                if(j[0] == i and j[1] == "&"):
                    aux = matrizDeTransicao.get(j)
                    if type(aux) == int:
                        lista.append(aux)
                    else:
                        for a in aux:
                            lista.append(a)
        
        fecho = []
        for i in lista:
            if(i not in fecho):
                fecho.append(i)
        fecho.sort()

        #print("fecho-&(",automato, ") = ", fecho)

        return fecho
    
    def uniaoDeEstados(self, estados):
        pass

    #verfica se o conjunto de estados "estados" tem algum estado final
    def temEstadoFinal(self, automato, estados):
        for i in estados:
            if(i == automato.estadosFinais):
                return True
        
        return False

    def transicao(self, estado, simbolo, automato):

        if estado:
            e = estado.pop()
            print("e: ", e)
        else:
            return " "
        #print("estado: ", estado)
        #print("simbolo: ", simbolo)
        
        for i in automato.matrizDeTransicao:
            #print("entra estado: ", i[0])
            #print("e entra simbolo: ", i[1])
            #print("sai estado: ", automato.matrizDeTransicao.get(i))
            print("estado: ", i[0], e)
            print("simbolo: ", i[1], simbolo)
            if(i[0] == e and i[i] == simbolo):
                #print(automato.matrizDeTransicao.get(i))
                print("entrou no if")
                return automato.matrizDeTransicao.get(i)
        
        return " "



    def gerarAFD(self, automato):
        afd = Automato()
        count = 0
        aux = ""
        equivalenciaDeEstados = {}
        #print(automato.estados)
        
        #base
        afd.estadoInicial = self.fechoE(automato.matrizDeTransicao, 0)
        print(afd.estadoInicial)
        afd.estados.append(0)
        equivalenciaDeEstados[0] = afd.estadoInicial

        if(self.temEstadoFinal(automato, afd.estadoInicial)):
            afd.estadosFinais.append(0)
        

        print(equivalenciaDeEstados)


        #indução
        for i in afd.estados:
            for j in automato.alfabeto:
                for k in equivalenciaDeEstados.values():
                    #print(k, j)
                    #print("------")
                    aux = aux + self.transicao(k, j, automato)

        print("aux: ", aux)
