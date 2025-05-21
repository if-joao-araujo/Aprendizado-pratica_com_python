"""8. Sejam a e b os catetos de um triangulo, onde a hipotenusa e obtida pela equacao: 
hipotenusa =
√ a**2 + b**2. Faca uma funcao que receba os valores de  ̃a e b e calcule o
valor da hipotenusa atraves da equacao.  ̃"""

def hipotenusa(a,b):
    hipo = ((a**2)+(b**2))**0.5
    return hipo

a = int(input("digite o valor a---> "))
b = int(input("digite o valor b---> "))
print(hipotenusa(a,b))

#concluido em 3 minutos e 43 segundos