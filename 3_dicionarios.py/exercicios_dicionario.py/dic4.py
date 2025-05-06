"""Crie um programa que gerencie uma agenda de contatos (nome → telefone) 
usando um dicionário. Inclua funções para adicionar, buscar e listar contatos."""

def contato():
    contador  = 1
    condicao = False
    dic = {}
    item = 0
    while  condicao == False:
        opcao = int(input("deseja adicionar contato[1],[2] para excluir ou [3] sair --> "))
        if opcao == 1:
            
            nome   = input("digite o nome--> ")
            numero = input("digite o numero--> ")
            dic[f"chave{contador}"] = {"nome": nome, "numero": numero}
            print(f"{dic[f"chave{contador}"]} --> adicionado com sucesso\n")
            contador +=1
    
        elif opcao == 2:
            print(f"numeros disponiveis: {dic}:  \n")
            exclusao = input("deseja excluir qual contato ex: chave1, chave2....--> ")
            if exclusao in dic:
               excluido = dic.pop(exclusao)
               print(f"{excluido} excluido com sucesso ")   
            else:
                print(f" contato não encontrado\n")

        elif opcao == 3:
             for c in dic.items():
                 print(c)  
             condicao = True  

contato()