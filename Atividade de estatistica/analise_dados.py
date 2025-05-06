

import csv
from random import uniform
from statistics import mean, median, mode


altura_alunos = {}

for i in range(1, 51):
    altura = round(uniform(1.40, 1.80), 2)
    altura_alunos[f"aluna {i}"] = altura

for i in range(1, 51):
    altura = round(uniform(1.50, 1.95), 2)
    altura_alunos[f"aluno {i}"] = altura


for nome, altura in altura_alunos.items():
    print(f"{nome}: {altura} m")



with open("alturas.csv", mode="w", newline="") as arquivo:
    escritor = csv.writer(arquivo)
    escritor.writerow(["Nome", "Altura (m)"])  
    for nome, altura in altura_alunos.items():
        escritor.writerow([nome, altura])

print("Arquivo 'alturas.csv' criado com sucesso!")


def mostrar_estatisticas(dados, genero):
    alturas = [altura for nome, altura in dados.items() if genero in nome]
    
    print(f"\nEstatísticas para {genero}s:")
    print(f"Quantidade: {len(alturas)}")
    print(f"Média: {round(mean(alturas), 2)} m")
    print(f"Mediana: {round(median(alturas), 2)} m")
    
    try:
        moda_valor = mode(alturas)
        print(f"Moda: {moda_valor} m")
    except:
        print("Moda: Não há moda única.")

mostrar_estatisticas(altura_alunos, "aluna")
mostrar_estatisticas(altura_alunos, "aluno")
