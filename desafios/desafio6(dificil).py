"""Faca um programa para gerar automaticamente numeros entre 0 e 99 de uma cartela de  ́
bingo. Sabendo que cada cartela devera conter 5 linhas de 5 numeros, gere estes dados  ́
de modo a nao ter numeros repetidos dentro das cartelas. O programa deve exibir na  ́
tela a cartela gerada."""
from random import randint

matriz = []

for i in range(0,5):
    linha = []
    for j in range(0,5):
        numero = randint(0,99)
        while numero in matriz:  
            numero = randint(0,99)
        
        linha.append(numero)
    matriz.append(linha)
print("### resultado do bingo ###")
for linhas in matriz:
    for valor in linhas:
        print(valor, end = " ")
    print()