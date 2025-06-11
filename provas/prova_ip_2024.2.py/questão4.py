"""Faça um programa que permita ao usuário entrar com a quantidade de
linhas (i) e a quantidade de colunas (j) de uma matriz de números 
inteiros. Peça ao usuário cada valor da matriz. Em seguida, gere uma 
lista com soma dos números de cada coluna da matriz e
mostre na tela essa lista (2,5 pontos). Por exemplo, se o usuário 
informar 3 linhas e 3 colunas, ele poderá preencher uma matriz
3x3. Supondo que a matriz abaixo foi digitada pelo usuário,

Na lista gerada, cada posição é a soma das colunas da matriz informada.
A primeira posição será 5 + 1 + 25, e assim por diante:
[ 31, 4, 32 ]"""

l = int(input("deseja quantas linhas na matriz--> "))
c = int(input("deseja quantas colunas na matriz -->"))
soma = 0
coluna_somadas = []
matriz = []
for i in range(l):
    linha = []
    for j in range(c):
        Numero = int(input(f"Digite os valores: [{i}][{j}] --> "))
        linha.append(Numero)
    soma +=Numero
    coluna_somadas.append(soma)
    matriz.append(linha)

print("#"*10,"Matriz","#"*10)

for linhas_de_matriz in matriz:
    for elementos_da_matriz in linhas_de_matriz:
        print(elementos_da_matriz, end=" ")
    print()

print(f"Soma da coluna {soma} lista com elementos de cada coluna  {coluna_somadas}")

#Depois eu concluo a logica da coluna