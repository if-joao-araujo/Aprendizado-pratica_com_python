"""Crie uma função recursiva que some os números naturais de 1 até N."""

def soma(n):
    if n <1:
        return 0
    else:
        return n + soma(n-1)

print(soma(4))

def fatorial(n):
    if n <1:
        return 1
    else:
        return n * fatorial(n -1)

print(fatorial(5))