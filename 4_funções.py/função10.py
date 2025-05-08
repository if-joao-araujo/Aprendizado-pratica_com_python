"""Crie uma func ̧ao recursiva que receba dois inteiros positivos 
k e n e calcule k**n
."""

def elevado(k,n):
    if k ==0 :
        return 1
    else:
        return k**2
    
    
k = int(input("digite um valor: "))
n = int(input(f"deseja elevar {k} a quanto: "))
print(elevado(k, n))

#concluido em 1 minuto e 59 segundos