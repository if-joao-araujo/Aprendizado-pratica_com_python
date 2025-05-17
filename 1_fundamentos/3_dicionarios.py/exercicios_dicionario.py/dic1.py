"""Crie um dicionário vazio e adicione 3 pares chave-valor (ex.: {"nome": "Alice", "idade": 25})."""
dic = {"Nome:": "","idade:":"","sexo:":""}

for c in dic:
    dic[c] = input(f"digite o {c} ---> ")

print(dic["Nome:"])
print(dic["idade:"])
print(dic["sexo:"])