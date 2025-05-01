"4 jogadores irão sortear dados, e terá um ranking em ordem crescente!"
from random import randint


jogadores = {"jogador1":randint(0,6),"jogador2":randint(0,6),"jogador3":randint(0,6),"jogador4":randint(0,6)}
ranking = {}
maior = 0
for c in jogadores.items():
   print(f"---> {c} ")
   if jogadores.values() > maior:
      maior = c
print(maior)