"""Diagonal Principal e Secundária
Peça uma matriz 3x3 e mostre a diagonal principal e a diagonal secundária separadamente."""
matriz = []
diagnonal_principal = []
diagonal_segundaria = []
contador_linhas_colunas = 3

for i in range(0,3):
    linha = []
    for j in range(0,3):
        numero = int(input(f"Digite o valor [{i}]:[{j}] --> "))
        linha.append(numero)
        if i == j:
            diagnonal_principal.append(numero)
    matriz.append(linha)
    

for linhas in matriz:
    for elementos in linhas:
        print(f" [{elementos}] ", end=" ")
    print()
print(f"Diagonal principal {diagnonal_principal}")
