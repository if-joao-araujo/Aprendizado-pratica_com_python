"""7. Fac ̧a uma funcao recursiva que receba um numero inteiro positivo N e 
imprima todos os numeros naturais de 0 ate N em ordem crescente.  ́"""

def ate_n(n):
    if n > 0:
       ate_n(n-1)
       print(n)

print(ate_n(5))