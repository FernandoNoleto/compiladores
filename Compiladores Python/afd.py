from afnd import Automato
import pprint

class AutomatoFinito(Automato):
    
    def __init__(self):
        super().__init__()

    #Matriz de transição e automato->int
    #estado = qual estado (int) quero calcular o fechoE
    def fechoE(self, matrizDeTransicao, estado):
        lista = []
        lista.append(estado)
        
        for i in matrizDeTransicao:
            if(i[0] == estado and i[1] == "&"):    
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
    #automato = afnd()
    def temEstadoFinal(self, automato, estados):
        for i in estados:
            if(i == automato.estadosFinais):
                return True
        
        return False

    def transicao(self, estado, simbolo, automato):
        
        for i in automato.matrizDeTransicao:
            #print('estado: ', estado)
            #print('simbolo: ', simbolo)
            #print("entra estado: ", i[0])
            #print("e entra simbolo: ", i[1])
            #print("sai estado: ", automato.matrizDeTransicao.get(i))
            
            if(i[0] == estado and i[1] == simbolo):
                #print("entrou no if")
                #print(automato.matrizDeTransicao.get(i))
                return automato.matrizDeTransicao.get(i)
        
        #return " "


    def lista_esta_no_dicionario(self, lista, dicionario):
        flag = False

        for i in dicionario.values():
            if i == lista:
                flag = True
        
        #print('lista esta no dicionario: ', flag)
        return flag

    def gerarAFD(self, automato):
        afd = Automato()
        count = 1
        equivalenciaDeEstados = {}
        estados_aux = []
        fecho_da_uniao = []
        lista_aux = []
        flag = False #tratar o fechoE que não retorna nada -> vazio

        #base
        afd.estadoInicial = 0
        equivalenciaDeEstados[0] = self.fechoE(automato.matrizDeTransicao, 0)
        estados_aux.append(equivalenciaDeEstados[0])
        #afd.estados.append(afd.estadoInicial)

        uniao = [] #união dos estado retornados da função de transição
        #indução
        #i = 
        #j = simbolo do alfabeto
        #k = estados internos (lista retornada do fechoE)
        o = 1
        #for i in list(equivalenciaDeEstados): #afd 
        q = 0
        while equivalenciaDeEstados:
            for i in list(equivalenciaDeEstados): #afd
                print('entrou ', o, ' vezes no primeiro for')
                o += 1
                estados_internos = equivalenciaDeEstados.get(i)
                    
                for j in automato.alfabeto: #simbolo do alfabeto
            
                    flag = False
                    uniao.clear()
                    fecho_da_uniao.clear()
                    lista_aux.clear()
                        
                    for k in estados_internos: #estados internos (fechoE)
                        t = self.transicao(k, j, automato)
                        if t: #para verificar se tem transição (pode ser que não tenho transição nenhuma dependendo do símbolo)
                            flag = True
                            uniao.append(t) #uniao dos estados retornados da função de transição
                        
                    if flag == False: #significa que o fechoE retornou vazio (estado vazio)
                        fecho_da_uniao.append(-1)
                    else:
                        for l in uniao:
                            lista_aux.append(self.fechoE(automato.matrizDeTransicao, l))
                        for l in lista_aux:
                            fecho_da_uniao += l
                    #print('fecho da uniao: ', fecho_da_uniao)
                    #return

                    #if fecho_da_uniao not in equivalenciaDeEstados:
                    if not self.lista_esta_no_dicionario(fecho_da_uniao, equivalenciaDeEstados): #se o estado gerado ainda não esta na lista de estados
                        print('estado novo!')
                        equivalenciaDeEstados[count] = fecho_da_uniao
                        afd.estados.append(count)
            
                    afd.matrizDeTransicao[(count - 1, j)] = len(equivalenciaDeEstados) - 1
                q += 1    
                count += 1
                #print('q = ', q)
                #print('len = ', len(equivalenciaDeEstados))
                #equivalenciaDeEstados = equivalenciaDeEstados.copy()
            if q > len(equivalenciaDeEstados):
                break

        pprint.pprint(afd.matrizDeTransicao)
                