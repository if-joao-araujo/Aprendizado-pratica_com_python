"""Leia uma matriz 4 x 4, conte e escreva quantos valores maiores que 10 
ela possui."""


maior_10 = 0
matriz = []
for i in range(0,4):
    linha = []
    for j in range(0,4):
        valor = int(input(f" digite os elementos {[i], [j]}--> "))
        linha.append(valor)
    matriz.append(linha)
            

for linhas in matriz:
    for colunas in linhas:
        print(f"[ {colunas} ]", end=" ")
        if colunas > 10:
            maior_10 +=1
    print()
print(f"valores maiores que 10: {maior_10}")

#demorei 17 minutos para fazer