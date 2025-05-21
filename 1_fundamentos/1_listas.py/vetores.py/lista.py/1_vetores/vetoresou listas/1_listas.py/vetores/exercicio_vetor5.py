"""Faca um programa que leia um vetor de 5 posic ̧oes para numeros reais e, depois, um 
codigo inteiro. Se o codigo for zero, finalize o programa; se for 1, mostre o vetor na ordem
direta; se for 2, mostre o vetor na ordem inversa. Caso, o codigo for diferente de 1 e 2 
escreva uma mensagem informando que o codigo  ́e invalido.  ́"""

vetor = []

for c in range(1,6):
    num = float(input(F"digite o numero{c} --> "))
    vetor.append(num)

num = int(input("digite o numero inteiro: "))
vetor.append(num)

opcao = int(input("escolha alguma opção --> [0] cancelar.\ [1] mostrar o vetor em ordem direta.\n "
"[2] mostrar em ordem inversa.\n ---->  "))
if opcao == 0:
    print("programa finalizado")
elif opcao == 1:
    print(f"os numeros digitados foram\n {vetor}")
elif opcao == 2:
    vetor_inverso = vetor[:: -1]
    print(f"o vetor em ordem inversa {vetor_inverso}")
else:
    print("numero invalido!!")

#demorei 11.57 minutos para completar esse exercicio