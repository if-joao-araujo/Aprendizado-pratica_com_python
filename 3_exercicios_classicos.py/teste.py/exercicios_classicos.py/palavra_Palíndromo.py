"verifique se a palavra é Palíndromo, palavras Palíndromo são iguais, idependente se for da "
"esquerda ou direita. exemplo: ovo, ana."

def Palíndromo(palavra):
    if palavra == palavra[::-1]:
        return 'é Palíndromo'
    else:
        return 'não é Palíndromo'

palavra = input("digite a palavra: ")
print(Palíndromo(palavra))