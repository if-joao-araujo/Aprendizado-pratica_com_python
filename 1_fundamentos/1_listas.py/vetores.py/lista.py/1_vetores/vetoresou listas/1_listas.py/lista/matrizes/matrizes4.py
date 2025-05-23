"""6. Leia duas matrizes 4 x 4 e escreva uma terceira com os maiores valores de cada posicao
das matrizes lidas."""

matriz1 = []
matriz2 = []
matriz3 = []


for i in range(0,4):
    linha = []
    for j in range(0,4):
        num = int(input(f"digite o elemento [{i}][{j}] da primeira matriz--> "))
        linha.append(num)
    matriz1.append(linha)

for k in range(0,4):
    linha2 = []
    for l in range(0,4):
        num2 = int(input(f"digite o elemento [{k}][{l}] da segunda matriz--> "))
        linha2.append(num2)
    matriz2.append(linha2)


for i2 in range(4):
    elemento_matriz3 = []
    for j2 in range(4):
        if matriz1[i2][j2] > matriz2[i2][j2]:
           maior = matriz1[i2][j2]
           elemento_matriz3.append(maior)
        else:
            maior = matriz2[i2][j2]
            elemento_matriz3.append(maior)
    matriz3.append(elemento_matriz3)

for x in matriz3:
    for y in x:
        print(x, end= " ")
    print()

#concluido em 40 minutos