#Função que verifica se a expressão é válida
def expressao_valida(expressao):
    a = [expressao.count('('),expressao.count(')'),expressao[0] != ')',expressao[-1]]
    if(expressao.count('(') == expressao.count(')') and expressao[0] != ')' and expressao[-1] != '(' and expressao[0] != '+'):
        return True
    else:
        return False

#Função que verifica se o operador é válido retornando TRUE ou FALSE
def operador_valido(operador):
    if(operador == '+' or operador == '*' or operador == '.' or operador == '(' or operador == ')' ):
        return True
    else:
        return False

#Função que verifica a prioridade do operador ou se é igual: retorna TRUE ou FALSE
def prioridade(operador_atual, operador2):

    if(operador2 == '*' and (operador_atual == '+' or operador_atual == '.')):
        return True
    elif(operador2 == operador_atual):
        return True
    elif((operador_atual == '.') and (operador2 == '*')):
        return True
    else:
        False

#Função que recebe a expressão e adiciona o operador "." na concatenação implícita.
def expressao_perfeita(expressao):
    i = 0
    aux = ''  #string que vai se concatenada com o decorrer do laço para colocar a cocatenação implicíta.
    j = 0
    ultimo_simbolo = expressao[-1]

    #Laço que vai percorrer a expressão e colocar os "." onde é implícito
    while(i < len(expressao)-1):
        aux += expressao[i]
        j += 1
        if(expressao[i] == '('):
            i += 1
            continue
        if(ultimo_simbolo != expressao[i] or i != len(expressao)-1):
            aux2 = expressao[i+1]
            if(expressao[i+1] != '*' and expressao[i+1] != '+'):
                if(expressao[i] == '+'):
                    i += 1
                    continue
                copyString = aux
                aux += '.'
                if((aux[j-1] == '(' and aux[j] == '.') or (aux[j] == '.' and expressao[i+1] == ')')):
                    aux = copyString
                    i += 1
                    #j += 1
                    continue
                j += 1
            i += 1
    aux += ultimo_simbolo
    return aux

#expressão que converte a expressão perfeita para pósfixa
def polonesa_reversa(expressao):
    expressao_reversa = '' #String para formar a pósfixa

    pilha = []
    for i in expressao:
        if(operador_valido(i)):
            if(i == ')'):
                #expressao_reversa += pilha[-1]
                while(pilha[-1] != '('):
                    expressao_reversa += pilha[-1]
                    pilha.pop()
                pilha.pop()
                continue
            if(pilha):
                if(prioridade(i,pilha[-1])):
                    expressao_reversa += pilha.pop()
                if(pilha):
                    if(prioridade(i,pilha[-1])):
                        expressao_reversa += pilha.pop()
            pilha.append(i)
        else:
            expressao_reversa += i
    while (pilha):
        expressao_reversa += pilha.pop()
    return expressao_reversa



