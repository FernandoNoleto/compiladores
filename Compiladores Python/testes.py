import f_posfixa

#Arquivo só para testes

def teste():
    if(f_posfixa.expressao_perfeita("a+b+c") == "a+b+c" and f_posfixa.polonesa_reversa("a+b+c") == "ab+c+"):
        print("Teste a+b+c = TRUE " + f_posfixa.expressao_perfeita("a+b+c") + " PósFixa " + f_posfixa.polonesa_reversa("a+b+c"))
    else:
        print("Teste a+b+c = FALSE " + f_posfixa.expressao_perfeita("a+b+c"))

    if (f_posfixa.expressao_perfeita("(a+b)") == "(a+b)" and f_posfixa.polonesa_reversa("(a+b)") == "ab+"):
        print("Teste (a+b) = TRUE " + f_posfixa.expressao_perfeita("(a+b)") + " PósFixa " + f_posfixa.polonesa_reversa("(a+b)"))
    else:
        print("Teste (a+b) = FALSE " + f_posfixa.expressao_perfeita("(a+b)"))

    if (f_posfixa.expressao_perfeita("ab") == "a.b" and f_posfixa.polonesa_reversa("a.b") == "ab."):
        print("Teste ab = TRUE " + f_posfixa.expressao_perfeita("ab") + " PósFixa " + f_posfixa.polonesa_reversa("a.b" ))
    else:
        print("Teste ab = FALSE " + f_posfixa.expressao_perfeita("ab"))

    if (f_posfixa.expressao_perfeita("a+bc(aa*b)*") == "a+b.c.(a.a*.b)*" and f_posfixa.polonesa_reversa("a+b.c.(a.a*.b)*") == "abc.aa*.b.*.+"):
        print("Teste a+bc(aa*b)* = TRUE " + f_posfixa.expressao_perfeita("a+bc(aa*b)*") + " PósFixa " + f_posfixa.polonesa_reversa("a+b.c.(a.a*.b)*"))
    else:
        print("Teste a+bc(aa*b)* = FALSE " + f_posfixa.expressao_perfeita("a+bc(aa*b)*"))

    if (f_posfixa.expressao_perfeita("(a+b)*(c+d)") == "(a+b)*.(c+d)" and f_posfixa.polonesa_reversa("(a+b)*.(c+d)") == "ab+*cd+."):
        print("Teste (a+b)*(c+d) = TRUE " + f_posfixa.expressao_perfeita("(a+b)*(c+d)") + " PósFixa " + f_posfixa.polonesa_reversa("(a+b)*.(c+d)"))
    else:
        print("Teste (a+b)*(c+d) = FALSE " + f_posfixa.expressao_perfeita("(a+b)*(c+d)"))

    if (f_posfixa.expressao_perfeita("a+(b+c)*(d+e)") == "a+(b+c)*.(d+e)" and f_posfixa.polonesa_reversa("a+(b+c)*.(d+e)") == "abc+*de+.+"):
        print("Teste a+(b+c)*(d+e) = TRUE " + f_posfixa.expressao_perfeita("(a+b)*(c+d)") + " PósFixa " + f_posfixa.polonesa_reversa("a+(b+c)*.(d+e)"))
    else:
        print("Teste a+(b+c)*(d+e) = FALSE " + f_posfixa.expressao_perfeita("(a+b)*(c+d)"))

    if (f_posfixa.expressao_perfeita("(0+(1(01*(00)*0)*1)*)*") == "(0+(1.(0.1*.(0.0)*.0)*.1)*)*" and f_posfixa.polonesa_reversa("(0+(1.(0.1*.(0.0)*.0)*.1)*)*") == "0101*.00.*.0.*.1.*+*"):
        print("Teste (0+(1(01*(00)*0)*1)*)* = TRUE " + f_posfixa.expressao_perfeita("(0+(1(01*(00)*0)*1)*)*") + " PósFixa " + f_posfixa.polonesa_reversa("(0+(1.(0.1*.(0.0)*.0)*.1)*)*"))
    else:
        print("Teste (0+(1(01*(00)*0)*1)*)* = FALSE " + f_posfixa.expressao_perfeita("(0+(1(01*(00)*0)*1)*)*"))