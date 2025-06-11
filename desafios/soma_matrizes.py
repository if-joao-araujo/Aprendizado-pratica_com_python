def matrizes():
    matriz_1 = []
    matriz_2 = []
    soma_matrizes = []

    print("Construa a Primeira matriz")

    for i1 in range(3):
        linha1 = []
        for j1 in range(3):
            numero = int(input(f"Digite valores [{i1}][{j1}]]"))
            linha1.append(numero)
        matriz_1.append(linha1)

    print("construa a Segunda matriz")

    for i2 in range(3):
        linha2 = []
        for j2 in range(3):
            numero = int(input(f"Digite valores [{i2}][{j2}]]"))
            linha2.append(numero)
        matriz_2.append(linha2)

    print("primeira Matriz: ")  
    for elemtentos_da_matriz in matriz_1:
        for elementos_de_elementos in elemtentos_da_matriz:
            print(f"[{elementos_de_elementos}]",end=" ")
           
        print()
    print("Segunda matriz: ")
    for elementos_da_matriz2 in matriz_2:
        for elemntos_de_elementos2 in elementos_da_matriz2:
            print(f"[{elemntos_de_elementos2 }]",end=" ")
        print()

    print("Matrizes somadas: ")

    for x  in range(3):
       linha = []
       for y in range(3):
           linha.append(matriz_1[x][y] + matriz_2[x][y])
       soma_matrizes.append(linha)
    
    for linhas in soma_matrizes:
        for resultado in linhas:
            print(f" [{resultado}] ", end=" ")
        print()
    return "Sucesso"   
print(matrizes())
