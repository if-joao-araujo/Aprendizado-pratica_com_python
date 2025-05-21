def fatorial(numero):
    if numero <=1:
        return 1
    return numero*(fatorial(numero - 1))

numero = int(input("digite um numero para ver o fatorial: "))
print(f"o fatorial de {numero} é igual a {fatorial(numero)}")