""".Em Matematica, o numero harmonico designado por ˆ H(n) define-se como sendo 
a soma da serie harmonica:  ́

H(n) = 1 + 1/2 + 1/3 + 1/4 + ... + 1/n

Fac ̧a um programa que leia um valor n inteiro e positivo e apresente 
o valor de H(n)."""
n = int(input("digite o valor: "))
soma = 0
for c in range(1,n+1):
    frac = 1/c
    soma += frac
    print(soma)

