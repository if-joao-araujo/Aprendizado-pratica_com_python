""")  Gere e imprima na tela uma matriz bidimensional de tamanho informado pelo usuário, 
onde seus elementos internos são definidos da seguinte forma: 
●  Se o índice da linha for menor que o índice da coluna, armazene na posição o valor 
da operação: 2 * i + 7 * j + 2 
●  Se o índice da coluna for igual ao índice da linha, armazene na posição o valor da 
operação: 3 * i2 + 1 
●  Se o índice da linha for maior que o índice da coluna, armazene na posição o valor 
da operação: 4 * i3 + 5 * j2 
 
sendo i o índice da linha e j o índice da coluna  (1,5 pontos). 
 
Exemplo:  
Quantidade de linhas: 2 
Quantidade de colunas: 2 
Impressão da matriz 2 x 2 
1     9 
4     4 """

matriz = []
quantidade_de_linhas = int(input("Digite a quantidade de linhas: "))
quantidade_de_colunas = int(input("Digite a quantidade de coluna: "))
for i in range(quantidade_de_linhas):
    linha = []
    for j in range(quantidade_de_colunas):
        if i <j:
            operacao = 2 * i + 7 * j + 2
        elif i==j:
            operacao = 3 * i**2 + 1 
        else:
            operacao =  4 * (i**3) + 5 * (j**2)
        linha.append(operacao)
    matriz.append(linha)
print(f"linhas {quantidade_de_linhas} | colunas {quantidade_de_colunas}")
for elementos in matriz:
    for elementos_de_elementos in elementos:
        print(f"[{elementos_de_elementos}]", end='')
    print()


