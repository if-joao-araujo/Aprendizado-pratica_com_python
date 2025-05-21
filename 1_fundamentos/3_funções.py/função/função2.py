"""3. Faca uma funcao para verificar se um numero e positivo ou negativo. Sendo que o valor
de retorno sera 1 se positivo, -1 se negativo e 0 se for igual a 0.  ́"""

def positivo_ou_negativo(num):
    if num >0:
        return 1
    elif num <0:
        return -1
    else:
        return 0

num = int(input("digite um numero: "))

print(positivo_ou_negativo(num))

#concluido em 3minutos