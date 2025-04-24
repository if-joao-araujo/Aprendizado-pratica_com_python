"""Fazer um programa para ler 5 valores e, em seguida, mostrar a posicao onde se 
encontram o maior e o menor valor."""

valores = []
maior = 0
menor = 1000

pos_menor = 0
pos_maior = 0
for c in range(1,6):
    num = int(input(f"digite o numero {c} --> "))
    if num > maior:
       maior = num
    if num < menor:
       menor = num
    valores.append(num)

for indice, valor in enumerate(valores):
    if maior == indice:
       pos_maior = indice
    if menor== valor:
       pos_menor = indice


print(f"o maior numero está na posição {pos_maior} que é o numero{valores[pos_maior]}\n")
print(f"o menor numero está na posição {pos_menor} que é o numero{valores[pos_menor]}\n")