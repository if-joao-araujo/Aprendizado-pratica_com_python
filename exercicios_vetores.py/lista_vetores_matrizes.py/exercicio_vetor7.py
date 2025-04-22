"""Fac ̧a um programa que receba 6 numeros inteiros e mostre:  ́
• Os numeros pares digitados;  ́
• A soma dos numeros pares digitados;  ́
• Os numeros  ́  ́ımpares digitados;
• A quantidade de numeros  ́  ́ımpares digitados;"""

vetor = []
par = []
soma_par = 0
impar = []
soma_impar = 0

for c in range(1,7):
    num = int(input(f"digite o numero {c} ---> "))
    if num % 2 == 0:
        par.append(num)
        soma_par += num
    else:
        impar.append(num)
        soma_impar += num
    vetor.append(num)
print(f" o numeros digitados foram ---> \n {vetor}\n")
print(f"os numeros pares digitados foram -->\n{par} e a soma deles é {soma_par}\n ")
print(f"os numeros impares digitados foram -- {impar}\n a soma deles é {soma_impar}")
 #demorei 9 minutos e 43 segundos para concluir