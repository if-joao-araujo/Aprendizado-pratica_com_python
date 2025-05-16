"""11. Elabore uma funcao que receba tres notas de um aluno como parametros e uma letra. ˆ
Se a letra for A, a funcao devera calcular a media aritmetica das notas do aluno; se for P,  ́
devera calcular a media ponderada, com pesos 5, 3 e 2.  ́"""
def nota_aluno():
    try:
        nota1 = float(input("digite a nota 1 --> "))
        nota2 = float(input("digite a nota 2 --> "))
        nota3 = float(input("digite a nota 3 --> "))
        opcao = input(" digite para calcular: [a] -> média aritimetica\n[p] -> média ponderada ").lower()
        if opcao == "a":
            print(f" a média aritimetica é igual {(nota1+nota2+nota3)/3}")
        elif opcao == "p":
            print(f"A média ponderada é -->\n {((nota1*5)+(nota2*3)+(nota3*2))/(5+2+3)}")
        else:
            print("opção invalida")
    except:
        print("digite apenas numeros!!!")
  

nota_aluno()