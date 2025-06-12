class Televisao:
   def __init__(self):
      self.canal = 2
      self.ligado = False
   def mudar_canal_para_baixo(self):
      self.canal -=1
      return self.canal
   def mudar_canal_para_cima(self):
        self.canal +=1
        return self.canal
   
tv = Televisao()
tv_da_sala = Televisao()

tv_da_sala.canal = 6
print(tv_da_sala.canal)
print(tv_da_sala.mudar_canal_para_cima())
print(tv.canal)
print(tv.ligado)