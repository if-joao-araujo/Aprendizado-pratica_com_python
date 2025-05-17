x = int(input("deseja quantas linhas na matriz--> "))
y = int(input("deseja quantas colunas na matriz -->"))
matriz = []
for i in range(0,x):
    linha = []
    for j in range(0,y):
        numero = int(input(f"digite o elemento [{i}][{j}] : "))
        linha.append(numero)
    matriz.append(linha)
soma_das_colunas = 0
for linhas in matriz:
    for colunas in linhas:
        print(f"[{colunas}]", end=" ")
    print()

