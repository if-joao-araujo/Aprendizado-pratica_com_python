#diagonal segundaria:
"""Seja uma matriz nxn, a diagonal secundária é formada pelos elementos cujas 
posições seguem a regra:
linha+coluna = n-1
ou
i+j=n-1. ex:
    0   1   2   -> colunas (j)
   [1] [2] [3]   0
   [4] [5] [6]   1
   [7] [8] [9]   2
   linhas (i)

   aqui temos uma matriz 3 por 3, então o primeiro elemento é 3-1 ==2
   então o primeiro elemento é 3, depois 2-1 ==1, então o segundo elemento será
   5, por fim 1-1, então o ultimo numero será 7.
   --> [3,5,7]
"""
#diagonal principal
""" seja nxn tal que linha seja igual a coluna ou i==j.
exemplo
          
0   1  2  -> colunas(j)
[1][2][3] 0
[4][5][6] 1  
[7][8][9] 2
linhas(i)   
linha 0 e coluna 0 == 1
linha 1 e coluna 1 == 5
linha 2 e coluna 2 == 9           
"""