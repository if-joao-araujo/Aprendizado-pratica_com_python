"""
Questão 3 (3,0 pontos)
Escreva um programa em Python que:**  
crie uma lista com 5 números inteiros digitados pelo usuário.  
Calcule e imprima:  
O maior número da lista.  
O menor número da lista.  
A média dos números.  

Exemplo:  
```
Digite um número: 10  
Digite um número: 20  
Digite um número: 5  
Digite um número: 15  
Digite um número: 25  
Maior: 25  
Menor: 5  
Média: 15.0  """

maior = 10**(-10)
menor = 10**10
soma = 0
lista = []
for c in range(5):
    numero = float(input("Digite um numero: "))
    soma += numero
    lista.append(numero)
    if numero > maior:
        maior = numero
    if numero < menor:
        menor = numero
print(f"Numeros digitados: {lista}")
print(f"Maior numero: {maior} Menor numero: {menor} ")
print(f"Media: {soma/len(lista)}")
