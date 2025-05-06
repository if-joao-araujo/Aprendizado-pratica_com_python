"""faça um programa que calcule uma função de segundo grau"""
"""A variavel a tem que ser diferente de zero. Caso seja igual, imprima a 
mensagem “Nao ̃e equacao de segundo grau”.  ̃
• Se ∆ < 0, nao existe real. Imprima a mensagem  ̃Nao existe raiz.
• Se ∆ = 0, existe uma raiz real. Imprima a raiz e a mensagem Raiz  ́unica.
• Se ∆ ≥ 0, imprima as duas raizes reais.
E ax2 + bx + c = 0 representa uma equac ̧ao de 2o grau."""

a = int(input("digite o valor de a "))
x = input("digite o valor de x ou o propio x--> ").lower()
if x == 'x':
    x = 1
elif type(x) is int:
    x = int(x)
elevado1 = int(input(f" o {x} está elevado a qual numero? "))
# vamos para o b
b = int(input("digite o valor de b "))
x2 = input("digite o valor de x ou o propio x--> ").lower()
if x2 == 'x':
    x2 = 1
elif type(x2) is int:
    x = int(x2)
elevado2 = int(input(f" o {x} está elevado a qual numero? "))

#valor de c 
c = int(input("c vale quanto: "))
ax = (a+x)**elevado1
bx = (b+x2)**elevado2
#delta --->>>
delta = (b)**2 - (4*a*c)
#raizes da equação
raizesx1 = (-bx + delta**0.5)/(2*a)
raizx2 = (-bx - delta**0.5)/(2*a) 


