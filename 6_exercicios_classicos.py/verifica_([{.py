
def verifica():
    cont = 1
    palavra = []
    while cont <=3:
        try :
            colchetes = input(f"digite o colchete[{cont}]: ")
            palavra.append(colchetes)
            cont +=1
        except:
            print("digite {,[ e ( ")

    chaves = []
    for pilha in palavra:
        chaves.append(pilha)
        if "{" in pilha:
            chaves.append("}")
        elif "[" in pilha:
             chaves.append("]")
        elif "(" in pilha:
             chaves.append(")")
    for c in chaves:
       print(c, end= " ")
    print()

verifica()