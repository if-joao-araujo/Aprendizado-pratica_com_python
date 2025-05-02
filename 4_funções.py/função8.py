"""Crie um programa que receba tres valores (obrigatoriamente maiores que zero), repre- 
sentando as medidas dos tres lados de um triangulo. Elabore funcoes para:  ̃

(a) Determinar se eles lados formam um triangulo, sabendo que: 
• O comprimento de cada lado de um triangulo e menor do que a soma dos outros  ́
dois lados.

(b) Determinar e mostrar o tipo de triangulo, caso as medidas formem um triangulo. 
Sendo que:
• Chama-se equilatero o triangulo que tem tres lados iguais. 
• Denominam-se isosceles o triangulo que tem o comprimento de dois lados
iguais.
• Recebe o nome de escaleno o triangulo que tem os tres lados diferentes. """

def triangulo(a,b,c):
    if (a > b+c) or (b > a+c) or (a <=0 )or (b<=0) or (c <= 0) :
        return "não é um triangulo"
    else:
        if a == b and b == c:
            return "é um triangulo equilatero"
        elif (a == b and a != c) or (b == c and b != a) or (c == a and c != b):
            return " é um triangulo isosceles"
        else: 
            return "é um triangulo escaleno"

a = int(input("digite o numero 1 --> "))
b = int(input("digite o numero 2 --> "))
c = int(input("digite o numero 3--> "))
print(triangulo(a,b,c))

#concluido em 13 minutos e 25 segundos