"""Faca uma funcao e um programa de teste para o calculo do volume de uma esfera.  ́
Sendo que o raio e passado por parametro. ˆ
V = 4/3 ∗ π ∗ R3"""

def esfera(r):
    pi = 3.14
    v = (4/3)*pi*(r**3)
    return v

r = int(input("digite o raio--> "))
print(esfera(r))

#concluido em 4 minutos e 45 segundos