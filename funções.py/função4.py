"""Fac ̧a uma func ̧ao para verificar se um numeroe um quadrado perfeito. Um quadrado  ́
perfeito e um n  ́ umero inteiro nao negativo que pode ser expresso como o quadrado de  ̃
outro numero inteiro. Ex: 1, 4, 9...  ́"""

def quadrado_perfeito(num):
    n = num**0.5
    n_int = int(n)
    if num <=0 :
        return "digite um numero maior que zero"
    else: 
        if n**2 == num:
          return f"{num} é um quadrado perfeito--> {n_int}"
        else:
            return f"{num} não é um quadrado perfeito---> {num**0.5}"
    

num = int(input("--> "))
print(quadrado_perfeito(num))
