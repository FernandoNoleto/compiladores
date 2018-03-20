#Função que verifica se a expressão é válida
def expressao_valida(expressao):
    i = 0
    try:
        if (expressao.index('\\')):
            j = 0
            while(j < len(expressao)):
                a = expressao[j]
                if(expressao[j] == '\\'):
                    j += 2
                    continue

                if(expressao[j] == '('):
                    i += 1
                    j += 1
                    continue
                if(expressao[j] == ')'):
                    i -= 1
                    j += 1
                    continue
                j += 1
        if(i == 0):
            return True
        else:
            return False

    except ValueError:

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
    elif((operador2 == operador_atual)):
        return True
    elif((operador_atual == '.') and (operador2 == '*')):
        return True
    elif(operador2 == '.' and operador_atual == "+"):
        return True
    else:
        return False
'''
#Função que recebe a expressão e adiciona o operador "." na concatenação implícita.
def expressao_perfeita_old(expressao):
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
            #aux2 = expressao[i+1]
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
def polonesa_reversa_old(expressao):
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
'''
#expressão que converte a expressão perfeita para pósfixa
def polonesa_reversa(expressao):
    expressao_reversa = '' #String para formar a pósfixa
    i = 0

    pilha = []
    while (i < len(expressao)):
        if(expressao[i] == '\\'):
            if(i+1 == len(expressao)):
                expressao_reversa += expressao[i]
                i += 1
            else:
                expressao_reversa += expressao[i] + expressao[i+1]
                i += 2
            #expressao_reversa += expressao[i]
                continue
        if(operador_valido(expressao[i])):
            if(expressao[i] == ')'):
                #expressao_reversa += pilha[-1]
                while(pilha[-1] != '('):
                    expressao_reversa += pilha[-1]
                    pilha.pop()
                pilha.pop()
                i += 1
                continue
            if(pilha):
                if(prioridade(expressao[i],pilha[-1])):
                    expressao_reversa += pilha.pop()
                if(pilha):
                    if(prioridade(expressao[i],pilha[-1])):
                        expressao_reversa += pilha.pop()
            pilha.append(expressao[i])
        else:
            expressao_reversa += expressao[i]
        i += 1
    while (pilha):
        expressao_reversa += pilha.pop()
    return expressao_reversa


#Função que recebe a expressão e adiciona o operador "." na concatenação implícita com \operador.
def expressao_perfeita(expressao):
    i = 0
    aux = ''  #string que vai se concatenada com o decorrer do laço para colocar a cocatenação implicíta.
    j = 0
    ultimo_simbolo = expressao[-1]

    #Laço que vai percorrer a expressão e colocar os "." onde é implícito
    while(i < len(expressao)-1):
        aux += expressao[i]
        j += 1

        if (expressao[i] == '\\' and i <= len(expressao)-3):
            if (expressao[i + 2] == '\\'):
                aux += expressao[i + 1] + '.'
                j += 2
            elif (expressao[i+2] == '('):
                aux += expressao[i + 1] + '.'
                j += 2
            else:
                aux += expressao[i+1]
                j += 1
            i += 2
            continue
        if(expressao[i] == '(' and expressao[i-1] != '\\'):
            i += 1
            continue
        if(ultimo_simbolo != expressao[i] or i != len(expressao)-1):
            #aux2 = expressao[i+1]
            if(expressao[i+1] != '*' and expressao[i+1] != '+' and expressao[i] != '\\'):
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



