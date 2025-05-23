"""Dados dois arrays classificados nums1e nums2de tamanho me nrespectivamente, retorne a mediana dos dois
 arrays classificados.
A complexidade geral do tempo de execução deve ser O(log (m+n)).
Exemplo 1:

Entrada: nums1 = [1,3], nums2 = [2]
 Saída: 2.00000
 Explicação: matriz mesclada = [1,2,3] e a mediana é 2.
Exemplo 2:

Entrada: nums1 = [1,2], nums2 = [3,4]
 Saída: 2,50000
 Explicação: matriz mesclada = [1,2,3,4] e a mediana é (2 + 3) / 2 = 2,5.
"""
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

