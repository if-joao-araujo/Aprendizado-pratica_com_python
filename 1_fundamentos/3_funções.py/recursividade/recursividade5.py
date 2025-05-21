def soma_total(numero):
    if numero<=1:
        return 0
    else:
        return numero + (soma_total(numero - 1)) 

numero = int(input("digite um numero: "))
print(soma_total(numero))