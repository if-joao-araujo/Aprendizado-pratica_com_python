"""24. Escreva uma funcao que gera um triangulo de altura e lados n e base 
2*n-1. Por exemplo, a saida para n = 6 seria:
*
***
*****
*******
*********
***********"""
def triangulo(n):
    asteristico = "*"
    mostrar_triangulo = ""
    for c in range(1,n+1):
        if c <=1:
           mostrar_triangulo = asteristico*c
           print(mostrar_triangulo )
        else:
            mostrar_triangulo = asteristico*(c*2 -1)
            print(mostrar_triangulo )

n = int(input("digite um numero: "))
triangulo(n)
