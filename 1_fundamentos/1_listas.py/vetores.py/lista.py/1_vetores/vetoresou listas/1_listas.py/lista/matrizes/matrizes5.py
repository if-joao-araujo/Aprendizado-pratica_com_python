"""10. Faca um programa para ler a nota da prova de 15 alunos e armazene num vetor
, calcule e imprima a media geral."""

alunos = {}
contador = 1
soma = 0
while contador<=15:
   nota = int(input(f"digite a nota do aluno {contador} --> "))
   alunos[f"Aluno{contador}: nota --> "] = nota
   soma += nota
   contador +=1

for c in alunos.items():
    print(c)
    print()
    
print(f"A média é {soma/15}")