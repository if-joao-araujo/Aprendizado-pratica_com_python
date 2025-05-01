"""Crie um programa que gerencie uma agenda de contatos (nome → telefone) 
usando um dicionário. Inclua funções para adicionar, buscar e listar contatos."""

def contato():
    contador  = 1
    condição = False
    dic = {}
    exclusao = 0
    item = 0
    while condição == False:
        opcao = int(input("deseja adicionar contato[1], ou [2] sair ou [3] para excluir --> "))
        if opcao == 1:
            nome   = input("digite o nome--> ")
            numero = input("digite o numero--> ")
            contador +=1
            dic["contato":contador] = {"nome": nome, "numero": numero}
            print(f"{dic["contato":contador]} --> adicionado com sucesso")
        elif opcao == 2:
          return dic 
        elif opcao == 3:
             print("contatos\n")
             for chave,valor in dic.items():  
                 print(f"{chave}: {valor} \n")
                 exclusao = input("deseja excluir qual contato--> ")
                 if exclusao in dic.items():
                    valor_excluido = dic.pop(exclusao)
                    print(f"{valor_excluido} excluido com sucesso ")
                 else:
                     print(f" contato não encontrado\n")
print(contato())