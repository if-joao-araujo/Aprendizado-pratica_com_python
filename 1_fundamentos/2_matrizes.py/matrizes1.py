"""Leia uma matriz 4 x 4, conte e escreva quantos valores maiores que 10 
ela possui."""



matriz = []
for i in range(0,4):
    linha = []
    for j in range(0,4):
        valor = int(input(f" digite os elementos {[i], [j]}--> "))
        linha.append(valor)
    matriz.append(linha)

for linhas in range(0,4):
    for colunas in matriz:
        print(colunas, end=" ")
    print()


#demorei 17 minutos para fazer