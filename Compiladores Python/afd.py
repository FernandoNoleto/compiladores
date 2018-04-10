class AutomatoFinito(object):
    
    def __init__(self):
        pass

    #Matriz de transição e automato->int
    def fechoDeKleene(self, matrizDeTransicao, automato):
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

    def transicoes(self, matrizDeTransicao):
        
        lista = []
        for i in matrizDeTransicao.keys():
            lista.append(self.fechoDeKleene(matrizDeTransicao, i[0]))
        
        print(lista)