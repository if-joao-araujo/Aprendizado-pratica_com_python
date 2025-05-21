"""3. Ler um conjunto de numeros reais, armazenando-o em vetor e calcular o quadrado das
componentes deste vetor, armazenando o resultado em outro vetor. Os conjuntos temˆ
10 elementos cada. Imprimir todos os conjuntos."""
conjunto =[]
vetor = []
for c in range(1,11,1):
    numero = float(input(f"Digite o elemento{c} --> "))
    conjunto.append(numero)
print(f" o conjunto 1 tem os elementos{conjunto}\n")
for elemento in conjunto:
    vetor.append(elemento**2)
print(f"o vetor criado com os elementos do conjunto1 ao quadrado é\n  {vetor}")

