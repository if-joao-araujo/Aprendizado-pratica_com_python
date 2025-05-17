"""Crie uma funcao recursiva que receba um n  ̃ umero inteiro positivo N e calcule o somatorio 
dos numeros de 1 a N.  ́"""

#sem recusividade
#def somatorio(n):
   # valor = 0
  # for soma in range(1,n+1):
     #  valor += soma
   #    print(f"{soma-1} + {soma} == {valor}")

#n = int(input("digite o numero: "))
#somatorio(n)

#com recusividade
def somatorio(n):
    if n <= 1:
        cont = 1
        return 1
    else:
        return n + somatorio(n-1)

n = int(input("digite um valor: "))
print(somatorio(n))