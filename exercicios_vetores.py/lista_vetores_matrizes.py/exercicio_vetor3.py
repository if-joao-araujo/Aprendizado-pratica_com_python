"""4. Fac ̧a um programa que leia um vetor de 8 posicoes e, em seguida, leia tambem dois 
valores X e Y quaisquer correspondentes a duas posicoes no vetor. Ao final seu programa  ̃
devera escrever a soma dos valores encontrados nas respectivas posic ̧  ́ oes  ̃ X e Y ."""
vetor = []
soma = 0
for c in range(1,9):
    num = int(input(f"digite o numero{c}---> "))
    vetor.append(num)

print(f"os numeros digitados foram\n {vetor}\n")
x = int(input("o numero x de qual indice  deseja soma--> "))
y = int(input("o numero y de qual indice deseja somar ---> "))
soma = vetor[x] + vetor[y]
print(f"a soma de {vetor[x]} + {vetor[y]} = {soma}")