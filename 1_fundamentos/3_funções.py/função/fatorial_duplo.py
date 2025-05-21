"""16. Faca uma func ̧ao recursiva que receba um numero inteiro positivo impar N e 
retorne o fatorial duplo desse numero. O fatorial duplo  ́ e definido como o produto de 
todos os numeros naturais  ́ımpares de 1 ate algum n  ́ umero natural ımpar N. Assim, o 
fatorial duplo de 5 e 
5!! = 1 * 3 * 5 = 15"""

def fatorial_duplo(num):
    if num <=1:
        return 1
    else:
      fat = 1
      for f in range(1,num+1):
         if f %2 !=0:
            fat*=f  
      return fat
    
num = int(input("digite o numero para ver o fatorial duplo: "))
print(fatorial_duplo(num))