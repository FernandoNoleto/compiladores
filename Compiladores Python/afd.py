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
    
    
    #passo o fechoE e retorno o estado a qual ele pertence
    def fechoE_reverso(self, matrizDeTransicao, fecho):
        
        for i in matrizDeTransicao:
            if self.fechoE(matrizDeTransicao, i[0]) == fecho:
                return i[0]
        
        return -1

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
        


    '''
    def lista_esta_no_dicionario(self, lista, dicionario):
        flag = False
        c = 0

        for i in dicionario.values():
            print('----------')
            print('lista: ', lista, 'd[', c, '] = ', i)
            print('----------')
            if i == lista:
                flag = True
            c += 1
        
        print('lista esta no dicionario: ', flag)
        return flag
    
    def adicionar_elemento_dicionario(self, dicionario, chave, valor):
        dicionario.update({chave: valor})

        return dicionario
    '''

    def estado_equivalente(self, dicionario, lista):
        for k, v in dicionario.items():
            if lista == v:
                return k
        return 0

    def gerarAFD(self, automato):
        afd = Automato()
        count = 1
        equivalenciaDeEstados = {}
        lista_de_estados_gerados = []
        fecho_da_uniao = []
        lista_aux = []
        lista_estados_em_fecho = []
        uniao = [] #união dos estado retornados da função de transição
        flag = False #tratar o fechoE que não retorna nada -> vazio
        w = 0
        q = 0

        
        #base
        afd.estadoInicial = 0
        afd.estados.append(0)
        equivalenciaDeEstados[0] = self.fechoE(automato.matrizDeTransicao, 0)
        lista_de_estados_gerados.insert(w, self.fechoE(automato.matrizDeTransicao, 0))
        w += 1
        lista_estados_em_fecho.append(self.fechoE(automato.matrizDeTransicao, 0))
        

        #verificar se o estado inicial também é final
        for i in fecho_da_uniao:
            if automato.estadosFinais == i:
                afd.estadosFinais.append(q)

        #indução
        #i = estados internos do fechoE
        #j = simbolo do alfabeto
        #k = estados internos (lista retornada do fechoE)
        #o = 1
        for i in lista_de_estados_gerados:

            estados_internos = i

                    
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
                
                if fecho_da_uniao not in lista_de_estados_gerados:
                    
                    lista_de_estados_gerados.insert(w, fecho_da_uniao.copy())
                    
                    w += 1
                    afd.estados.append(count)
                
                if fecho_da_uniao not in equivalenciaDeEstados.values():
                    equivalenciaDeEstados[count] = fecho_da_uniao.copy()

                afd.matrizDeTransicao[(q, j)] = self.estado_equivalente(equivalenciaDeEstados, fecho_da_uniao)
                
                for i in fecho_da_uniao:
                    if automato.estadosFinais == i and q not in afd.estadosFinais:
                        afd.estadosFinais.append(q)
                    
                count += 1
            q += 1
        
        
        
        
        print('---------------TRABALHO 3----------------')
        
        #imprimir todos os fechos-&
        for i in range(len(automato.matrizDeTransicao)):
            print('fechoE(', i, ') =', self.fechoE(automato.matrizDeTransicao, i))
        
        print('')
        
        pprint.pprint(afd.matrizDeTransicao)
        
        print('')

        print('Estado Inicial: ', afd.estadoInicial)
        print('Estados Finais: ', afd.estadosFinais)

        return afd
                