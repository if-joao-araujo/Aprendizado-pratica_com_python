"""Uma empresa de tecnologia está desenvolvendo um sistema que auxilia estudantes em cálculos matemáticos. Sua tarefa é criar um programa em Python que ajude os alunos a entender o conceito de fatorial de um número.
O fatorial de um número inteiro positivo n, representado por n!, é o produto de todos os números inteiros positivos de 1 até n. Por definição:
5! = 5 x 4 x 3 x 2 x 1 = 120
1! = 1
0! = 1 (por definição matemática)
Requisitos do programa:
Solicite ao usuário que digite um número inteiro não negativo.
Verifique se o número é válido (ou seja, maior ou igual a 0). Caso contrário, exiba uma mensagem de erro e repita a entrada."""

def fatorial(num):
    if num <=0:
        return 1
    else:
        return num * fatorial(num-1)

num = int(input("Digite um numero: "))
print(f"o fatorial de {num} é {fatorial(num)}!")
        