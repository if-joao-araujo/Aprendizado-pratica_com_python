"Crie uma função que receba um range e retorne um lista com apenas os numeros pares"

def lista_par(inicio, fim):
    lista = []
    for c in range(inicio,fim+1):
        numero = int(input(f"DIgite o numero: {c} --> "))
        if numero % 2 == 0 or numero == 0:
            lista.append(numero)
    if lista == []:
        return "Não foi digitado nehum numero par"
    else:
        return f"Numeros pares: {lista}"
    
inicio = int(input("Digite o inicio : "))
fim = int(input("Digite o final : "))
print(lista_par(inicio,fim))