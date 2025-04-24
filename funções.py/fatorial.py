def fatorial(num):
    fat = 1
    for c in range(num,0,-1):
        print(f"{c-1} x {c} = {fat}")
        fat *= c
    print(f"o fatorial de  {num} é igual a {fat}")

num = int(input("digite um numero: "))
fatorial(num)