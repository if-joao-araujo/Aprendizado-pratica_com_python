"""questão (1)"""
def tabuada(n,inicio,fim):
    cont = 1
    for c in range(inicio,fim+1):
        print(F"{n} x {c} == {n*c}\n")

print(tabuada(5,1,15))
