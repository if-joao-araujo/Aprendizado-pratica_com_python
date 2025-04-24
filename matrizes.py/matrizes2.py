"""Declare uma matriz 5 x 5. Preencha com 1 a diagonal principal e com 0 os demais
elementos. Escreva ao final a matriz obtida."""
matriz = []

for i in range(0,5):
    linha = []
    for j in range(0,5):
        num = int(input(f"digite o elemento [{i}][{j}]: "))
        if j != 2 and i !=2 :
           linha.append(num)
          
        else:
            linha.append(1) 
        matriz.append(linha)
for linhas in range(0,5):
    for colunas in range(0,5):
        print(matriz[linhas][colunas], end= " ")
    print()

    #concluido em 12minutos e 9 segundos

    