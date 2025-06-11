
matriz = []
n = int(input("digite a quantidade de linhas: "))
m = int(input("digite a quantidade de colunas: "))
soma = 0
contador = 0
for x in range(n):
    linha = []
    for y in range(m):
        numero = int(input(f"Digite o elemento [{x}][{y}]: "))
        contador +=1
        soma+=numero
        linha.append(numero)
    matriz.append(linha)

for linhas in matriz:
    for colunas in linhas:
        print([colunas], end = " ")
    print()
print(f"Mediana igual a {soma/contador}")

