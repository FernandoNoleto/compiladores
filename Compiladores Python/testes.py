from f_posfixa import Posfixa

#Arquivo só para testes

class Teste(object):
    
    def teste(self):
        pos = Posfixa()
        if(pos.expressao_perfeita("a+b+c") == "a+b+c" and pos.polonesa_reversa("a+b+c") == "ab+c+"):
            print("Teste a+b+c = TRUE " + pos.expressao_perfeita("a+b+c") + " PósFixa " + pos.polonesa_reversa("a+b+c"))
        else:
            print("Teste a+b+c = FALSE " + pos.expressao_perfeita("a+b+c"))

        if (pos.expressao_perfeita("(a+b)") == "(a+b)" and pos.polonesa_reversa("(a+b)") == "ab+"):
            print("Teste (a+b) = TRUE " + pos.expressao_perfeita("(a+b)") + " PósFixa " + pos.polonesa_reversa("(a+b)"))
        else:
            print("Teste (a+b) = FALSE " + pos.expressao_perfeita("(a+b)"))

        if (pos.expressao_perfeita("ab") == "a.b" and pos.polonesa_reversa("a.b") == "ab."):
            print("Teste ab = TRUE " + pos.expressao_perfeita("ab") + " PósFixa " + pos.polonesa_reversa("a.b" ))
        else:
            print("Teste ab = FALSE " + pos.expressao_perfeita("ab"))

        if (pos.expressao_perfeita("a+bc(aa*b)*") == "a+b.c.(a.a*.b)*" and pos.polonesa_reversa("a+b.c.(a.a*.b)*") == "abc.aa*.b.*.+"):
            print("Teste a+bc(aa*b)* = TRUE " + pos.expressao_perfeita("a+bc(aa*b)*") + " PósFixa " + pos.polonesa_reversa("a+b.c.(a.a*.b)*"))
        else:
            print("Teste a+bc(aa*b)* = FALSE " + pos.expressao_perfeita("a+bc(aa*b)*"))

        if (pos.expressao_perfeita("(a+b)*(c+d)") == "(a+b)*.(c+d)" and pos.polonesa_reversa("(a+b)*.(c+d)") == "ab+*cd+."):
            print("Teste (a+b)*(c+d) = TRUE " + pos.expressao_perfeita("(a+b)*(c+d)") + " PósFixa " + pos.polonesa_reversa("(a+b)*.(c+d)"))
        else:
            print("Teste (a+b)*(c+d) = FALSE " + pos.expressao_perfeita("(a+b)*(c+d)"))

        if (pos.expressao_perfeita("a+(b+c)*(d+e)") == "a+(b+c)*.(d+e)" and pos.polonesa_reversa("a+(b+c)*.(d+e)") == "abc+*de+.+"):
            print("Teste a+(b+c)*(d+e) = TRUE " + pos.expressao_perfeita("(a+b)*(c+d)") + " PósFixa " + pos.polonesa_reversa("a+(b+c)*.(d+e)"))
        else:
            print("Teste a+(b+c)*(d+e) = FALSE " + pos.expressao_perfeita("(a+b)*(c+d)"))

        if (pos.expressao_perfeita("(0+(1(01*(00)*0)*1)*)*") == "(0+(1.(0.1*.(0.0)*.0)*.1)*)*" and pos.polonesa_reversa("(0+(1.(0.1*.(0.0)*.0)*.1)*)*") == "0101*.00.*.0.*.1.*+*"):
            print("Teste (0+(1(01*(00)*0)*1)*)* = TRUE " + pos.expressao_perfeita("(0+(1(01*(00)*0)*1)*)*") + " PósFixa " + pos.polonesa_reversa("(0+(1.(0.1*.(0.0)*.0)*.1)*)*"))
        else:
            print("Teste (0+(1(01*(00)*0)*1)*)* = FALSE " + pos.expressao_perfeita("(0+(1(01*(00)*0)*1)*)*"))

        if (pos.expressao_perfeita("\*(\+\(*\))\*") == "\*.(\+.\(*.\)).\*" and pos.polonesa_reversa("\*.(\+.\(*.\)).\*") == "\*\+\(*.\)..\*."):
            print("Teste \*(\+\(*\))\* = TRUE " + pos.expressao_perfeita("\*(\+\(*\))\*") + " PósFixa " + pos.polonesa_reversa("\*.(\+.\(*.\)).\*"))
        else:
            print("Teste \*(\+\(*\))\* = FALSE " + pos.expressao_perfeita("\*(\+\(*\))\*"))