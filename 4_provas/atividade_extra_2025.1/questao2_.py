
gabarito = {}
provas = {}
notas = {}
for c in range(1,6):
    gabarito[f'questao{c}'] =input(f"Digite o gabarito da questão {c}: ")


for aluno_atual in range(1,6):
    print(f"####---------Prova do aluno {aluno_atual} --------####")
    questao = {}
    for numero_questao in range(1,6):
        resposta_aluno = input(f"Digite a resposta da questão {numero_questao}: ")
        questao[f"questao{numero_questao}"] = resposta_aluno
        provas[f"Aluno{aluno_atual}"] = questao
print()
for aluno, resposta in provas.items():
    notas[aluno] =0
    for numero in range(1,6):
        if resposta[f"questao{numero}"] ==  gabarito[f"questao{numero}"]:
            notas[aluno] +=2
        else:
            notas[aluno] +=0
for aluno_x, nota_final in notas.items():
    print(f"{aluno_x} | nota-->  {nota_final} pontos")
    print()
print("Gabarito oficial")
for q,r in gabarito.items():
   print(q, r)
percentual_de_aprovacao = notas[aluno] *100
print(f"Percentual de aprovação da turma ->  {percentual_de_aprovacao/25}%")

        

