"""Escreva um programa que leia um numero inteiro positivo n e em seguida imprima 
n linhas do chamado Triangulo de Pascal:
1
1 1
1 2 1
1 3 3 1
1 4 6 4 1
1 5 10 10 5 1"""

n = int(input("deseja fazer um triangulo com quantas linhas: "))
contador = "+"

for c in range(1,n+1):
    print(contador*c, end=" ")
    print()

#conclui em 3,20 segundos