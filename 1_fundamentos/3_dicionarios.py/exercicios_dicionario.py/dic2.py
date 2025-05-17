"""Crie um dicionário de estoque de produtos"""

lista = {}
condicao = True
contador = 1
while condicao == True:
   alimentos = {}
   alimentos["nome:"] = input("digite o nome do alimento: ")
   alimentos["preço:"] = input(f"digite o preço do {alimentos['nome:']}: ")
   alimentos["quantia:"] = input(f"digite a quantidade  do {alimentos['nome:']}: ")
   lista[contador] = alimentos.copy() 
   contador +=1
   opcao = input("clique em [s] para sair ou qualquer botão para continuar : ").lower()
   if opcao == "s":
       break

for chave,valor in lista.items():
    print(f"{valor}\n")