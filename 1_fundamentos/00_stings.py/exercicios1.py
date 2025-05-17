#exercicio 1
nome1 = input("digite o nome : ")
nome2 = input("digite o sobrenome: ")
print(f" nome  -> {nome1}. sobrenome  -> {nome2}.")
#exercicio 2
texto = input("digite um testo--> ")
texto_invertido = texto[::-1]
print(texto_invertido)
#exercicio 3 
palavra = input("digite uma palavra para verificar se é polidromo: ")
palavra_polidromo = palavra == palavra[::-1]
print(palavra_polidromo)
#estou fazendo sem if - else..... ,-,