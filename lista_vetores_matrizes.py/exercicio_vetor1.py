"""Faca um programa que possua um vetor denominado A que armazene 6 numeros intei-
ros. O programa deve executar os seguintes passos:
(a) Atribua os seguintes valores a esse vetor: 1, 0, 5, -2, -5, 7.
(b) Armazene em uma variavel inteira (simples) a soma entre os valores das posicoes  
A[0], A[1] e A[5] do vetor e mostre na tela esta soma.
(c) Modifique o vetor na posic ̧ao 4, atribuindo a esta posic ̧  ̃ ao o valor 100.  ̃
(d) Mostre na tela cada valor do vetor A, um em cada linha."""
vetor = [1,0,5,-2,-5,7]
soma = vetor[0]+vetor[1]+vetor[5]
for c in vetor:
   print(  c, end=" ")
   print()
print(f" a soma deu {soma}")
vetor[4] = 100
print("com a mudança ficou:\n")
for l in vetor:
   print(l, end="--> ")

