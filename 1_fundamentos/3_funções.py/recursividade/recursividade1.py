
def somatorio(n):
    if n <= 1:
        return 1
    else:
        return n + somatorio(n-1)

n = int(input("digite um valor: "))
print(somatorio(n))