""" Faca um programa que leia um numero inteiro N e depois imprima os N primeiros
numeros naturais  ́ımpares."""

def impar(n):
    print("numeros impares --> \n")
    for c in range(n+1):
        if c %2 == 1:
            print(c)

impar(9)