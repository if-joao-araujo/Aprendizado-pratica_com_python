"""A comissão organizadora de uma eleição para o grêmio estudantil quer criar um programa em Python que registre os votos dos alunos de uma turma.
Os candidatos à presidência do grêmio são identificados por códigos numéricos:

1 – Alice

2 – Bruno

3 – Carla

O sistema deve funcionar da seguinte forma:
Regras:
O programa deve pedir o número de eleitores.
Para cada eleitor, o programa deve solicitar um voto válido (entre 1 e 5). Caso o número digitado seja inválido, exibir uma mensagem de erro e repetir a entrada até que seja válido.
Os votos devem ser armazenados em uma lista.
Após o fim da votação, o programa deve:
Contar os votos para cada candidato 
Exibir o resultado final usando um dicionário, onde a chave é o nome do candidato e o valor é a quantidade de votos recebidos.
Exibir o candidato vencedor"""
contador = 1
numero_de_pessoas_a_votar = int(input("Quantas pessoas votarão: "))
votos = []
candidatos = {"Alice":0,"bruno":0,"carla":0}
while contador <= numero_de_pessoas_a_votar:
    print(f"vez do candidato {contador} votar!")
    candidato = int(input("Vote no candidato [1]: alice, [2]: bruno ou [3]: carla -->  ")) 
    if candidato < 1 or candidato>3:
        print("Digite um numero correto [1][2] ou [3]")
    else:
        votos.append(candidato)
        contador +=1

for apuracao_votos in votos:
    if apuracao_votos == 1:
        candidatos["Alice"] +=1
    elif apuracao_votos ==2:
       candidatos["bruno"] +=1
    else:
        candidatos["carla"] +=1

vencedor = []
for chave, valor in candidatos.items():
    print(f"Candidato: {chave} -> votos {valor}")
    vencedor.append(valor)

if vencedor[0] > vencedor[1] and vencedor[0]> vencedor[2]:
   print("Alice venceu")
elif vencedor[1] > vencedor[2] and vencedor[1]>vencedor[0]: 
    print("Bruno  venceu")
elif vencedor[2] > vencedor[0] and vencedor[2] >vencedor[1]:
     print("carla venceu")
else:
    print("houve um empate, a votação precisa ser reiniciada")