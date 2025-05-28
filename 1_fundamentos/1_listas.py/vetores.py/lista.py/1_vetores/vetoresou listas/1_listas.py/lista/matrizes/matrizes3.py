"""Fac ̧a um programa que preenche uma matriz com o produto do valor da linha e da coluna
de cada elemento. Em seguida, imprima na tela a matriz."""

matriz = []
produto = 1
for i in range(0,3):
    linha = []
    for j in range(0,3):
        num = int(input(f"digite o elemento [{i}][{j}]--> "))
        produto *= num
        linha.append(produto)
    matriz.append(linha) 

for linhas in matriz:
    for colunas in linhas:
        print(f" [{colunas}]  ", end= "  ")
    print()
