"""Questão 1: Crie um programa que gere uma sequência numérica personalizada de 
acordo com a entrada do usuário. O programa deve solicitar: (i) o número inicial 
da sequência, (ii) o número final da sequência e (iii) o valor do incremento entre
os números. Para cada número da sequência, mostre também seu valor ao quadrado e ao
cubo, conforme exemplo abaixo (0,5 pontos): 
Número inicial: 2
Número final: 6
Incremento: 2​
Sequência numérica personalizada:
Número: 2 | Quadrado: 4 | Cubo: 8
Número: 4 | Quadrado: 16 | Cubo: 64
Número: 6 | Quadrado: 36 | Cubo: 216"""

def sequencia(inicio,fim,incremento):
    for c in range(inicio,fim+incremento,incremento):
        print(f"--> {c} ao quadrado = {c**2};--> ao cubo = {c**3}\n.")

    
inicio = int(input("digite o inicio: "))
fim = int(input("digite o fim: "))
incremento = int(input("digite o incremento: "))
print(sequencia(inicio,fim,incremento))

#concluido em 10 minutos e 38 segundos
