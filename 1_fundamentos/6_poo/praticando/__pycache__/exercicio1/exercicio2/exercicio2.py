"""Exercício 10.2 Atualmente, a classe Televisão inicializa o canal com 2. Modifique
a classe Televisão de forma a receber o canal inicial em seu construtor."""
class Televisao:
   def __init__(self,min,max):
      self.canal = 2
      self.ligado = False
      self.max = max
      self.min = min
   def mudar_canal_para_baixo(self):
      self.canal -=1
      if self.canal - 1 <self.min:
          self.canal +=1
      return self.canal
   def mudar_canal_para_cima(self):
        self.canal +=1
        if self.canal > self.max:
            self.canal -=1
        return self.canal
   
   
tv = Televisao(1,20)
tv_da_sala = Televisao(1,20)

tv_da_sala.canal = 6
print(tv_da_sala.canal)
print(tv_da_sala.mudar_canal_para_cima())
for x in range(30):
    print(tv_da_sala.mudar_canal_para_cima())
