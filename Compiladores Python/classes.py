class Automato(object):
    
    estado_nome
    estado_destino
    simbolo_de_transicao
    aux_nome = 0
    
    
    def __init__(self, nome, destino, simbolo):
        self.estado_nome = nome
        self.estado_destino = destino
        self.simbolo_de_transicao = simbolo
    
    def entrada(entrada):
        for x in entrada:
            if x == '+': #concatenação
                concatenacao(x)
            else if x == '.': #união
                uniao(x)
            else if x == '*': #fecho de kleene
                fecho(x)
            else: #caso seja operando
                operando(x)

    def operando(x):
        a2 = Automato(aux_nome, '', '') #estado destino
        a1 = Automato(aux_nome, a2.estado_nome, x) #estado atual
        aux_nome += 1

    def concatenacao(self.simbolo):
        a1 = Automato('0', self.simbolo)
        a2 = Automato('1', )




        
    