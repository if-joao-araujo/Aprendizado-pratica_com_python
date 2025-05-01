"crie um dicionario que mostre se um aluno foi aprovado na média"
dic = {}

dic['nome'] = input("digite o nome do aluno--> ")
dic['media'] = int(input(f"digite a média de {dic['nome']} --> "))

if dic["media"] >=7:
    dic['situacao'] = 'aprovado'
elif dic["media"] <=6 and dic["media"] >=3:
    dic['situacao'] = 'recuperação'
else:
    dic["situacao"] = "reprovado"

for c in dic.items():
   print(f"---> {c}")
