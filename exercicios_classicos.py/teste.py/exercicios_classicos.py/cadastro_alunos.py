from time import sleep
alunos = {}
media = 0
while True:
    opcao = int(input("""digite uma opção:
                      [1] -> adicionar aluno.
                      [2] procurar contato do aluno
                      [3] remover aluno.
                      [4] mostrar todos contatos
                      [5] sair. --> """))
    if opcao == 1:
        aluno = input("digite o nome do aluno: ")
        nota1 = float(input("Digite a primeira nota do aluno: ")) 
        nota2 = float(input("Digite a segunda  nota do aluno: ")) 
        media = (nota1+nota2)/2
        alunos[aluno] = media


    elif opcao == 2:
        busca_aluno = input("Deseja encontrar qual aluno --> ")
        if busca_aluno in alunos.keys():
            print(alunos[busca_aluno])
        else:
            print("aluno não encontrado")

    elif opcao == 3:
        busca_aluno = input("deseja encontrar qual aluno: ")
        if busca_aluno in alunos.keys():
            alunos.pop(busca_aluno)
           
            print(f"aluno {busca_aluno} foi removido")
          
        else:
            print("aluno não existe")

    elif opcao == 4:
        if alunos == {}:
            print("Não tem alunos cadastrados")
        else:
            print("alunos cadastrados:   média: ")
            for aluno in alunos.items():
                print("="*50)
                print(aluno)
                print("="*50)

    elif opcao == 5:
        for c in alunos.items():
            print(c)
        print("encerrando programa...")
        sleep(2)
        break
    
    else:
        print("digite uma opção valida!!\n")