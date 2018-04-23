import re

class Regex(object):

    NUM = "^ *([0-9]*[0-9])$"
    OP1 = "^ *([+-])$"
    OP2 = "^ *([/*])$"
    A_PARENTESES = "^ *(()$"
    F_PARENTESES = "^ *())$"
    IF = "^ *(if)$"
    ELSE = "^ *(else)$"
    DO = "^ *(do)$"
    WHILE = "^ *(while)$"
    FOR = "^ *(for)$"
    A_CHAVES = "^ *({)$"
    F_CHAVES = "^ *(})$"
    PONTO_E_VIRGULA = "^ *(;)$"
    OP_REL = "^ *(>|<|>=|<=|!=|==)$"
    TIPO = "^ *(int|float|char|bool)$"
    #LITERAL = "^ *\"([\w :]|\")*\"$"
    #IDT = "^ *[_a-zA-Z][\w]*$"
    #ERRO = "^ *(\"|\"([\w :]|\")*)$"
    
    def match(self, linha):
        pass

    def main(self):
        #i = 0

        reg = re.compile(self.NUM)
        arq = open("entrada.txt", "r")
        texto = arq.readlines()
        for linha in texto:
            for char in linha:
                print(reg.match(char))
        arq.close()
        
        #reg = re.compile("[A-Z][a-z]*")
        #var = reg.match("fernando")
        #print (var)
        #print(reg.match("fernando") is None)
        
        #if var is None:
        #    print(var)

    

if __name__ == '__main__':
    regex = Regex()
    regex.main()