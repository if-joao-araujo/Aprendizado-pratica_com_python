from random import randint
from time import sleep
def zero_num(j1):
   j2 = randint(0,10)
   j3 = randint(0,10)
   j4 = randint(0,10)
   dedo = j1+j2+j3+j4
   if j1+j2+j3+j4 == 0 or j1 >10:
      return 1
   else:
      print(f"voçe jogou -->  {j1} dedos")
      sleep(0.5)
      print(f" o jogador 2 jogou -->  {j2} dedos" )
      sleep(0.5)
      print(f" o jogador 3 jogou -->  {j3} dedos" )
      sleep(0.5)
      print(f" o jogador 2 jogou -->  {j4} dedos" )
      sleep(0.5)
      print(f"Dedos jogados na rodada {dedo}")
      if dedo < 4:
         if dedo == 1:
            return "jogador 1 ganhou"
         elif dedo == 2:
            return "jogador 2 ganhou"
         elif dedo == 3:
              return "jogador 3 ganhou" 
      else:
         if dedo%4 == 0:
            return "jogador 4 ganhou"
         else:
            return f" o vencedor foi o jogador {dedo%4}"
j1 = int(input("jogue dedos: "))
print(zero_num(j1))