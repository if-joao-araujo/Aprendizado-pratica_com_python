"""Ler dois conjuntos de numeros reais, armazenando-os em vetores e calcular o produto  ́
escalar entre eles. Os conjuntos tem 5 elementos cada. Imprimir os dois conjuntos e o ˆ
produto escalar, sendo que o produto escalar e dado por:  ́ x1 ∗ y1 + x2 ∗ y2 + ... + xn ∗ yn."""

vetorx = []
vetory = []

for c in range(1,6):
    numx = float(input(f"digite o elemento x {c}-->"))
    vetorx.append(numx)
    numy = float(input(f"digite o elemento y {c}-->"))
    vetory.append(numy)
produto_escalar = 1

for i in range(len(vetorx)):
   produto_escalar += vetorx[i] * vetory[i]
print(produto_escalar)

#demorei 23 minutos para concluir