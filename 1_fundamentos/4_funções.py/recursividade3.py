"""Faca uma funcao recursiva que calcule e retorne o N-lesimo 
termo da sequencia Fibo-nacci. Alguns numeros desta sequencia 
são: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89...  ̃"""

"""A fórmula recursiva da sequência é:

f(n)=f(n-1)+f(n-2)F(n)=F(n-1)+F(n-2)

Com as condições iniciais:
f(0)= 0, f(1)= 1, F(0)= 0,F(1)=1 Ou seja, para calcular um termo, você soma os
 dois anteriores.
"""

def febonaci(n):
    if n <=1:
        return n
    return febonaci( n - 1 ) + febonaci(n - 2)

n = int(input("digite n: "))
print(febonaci(n))

#concluido em 14 minutos