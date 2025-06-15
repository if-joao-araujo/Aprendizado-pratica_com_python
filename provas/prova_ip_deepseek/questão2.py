"""
Questão 2 (2,5 pontos) 
Escreva um programa em Python que:**  
Peça ao usuário para digitar uma palavra.  
Verifique se a palavra é um **palíndromo** (ou seja, se ela é igual quando lida de trás para frente).  
imprima "É palíndromo" ou "Não é palíndromo".  """

palavra = input("Digite uma palavra: ").lower()
polidromo = palavra[::-1]

if palavra == polidromo:
    print("È polidromo")
else:
    print("Não é polidromo")