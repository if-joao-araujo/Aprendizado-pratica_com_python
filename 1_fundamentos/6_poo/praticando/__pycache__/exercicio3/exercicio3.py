"""Exercício 10.3 Modifique a classe Televisão de forma que, se pedirmos para mudar
o canal para baixo, além do mínimo, ela vá para o canal máximo. Se mudarmos
para cima, além do canal máximo, que volte ao canal mínimo. Exemplo:
> > > tv=Televisão(2,10)
> > > tv.muda_canal_para_baixo()
> > > tv.canal
10
> > > tv.muda_canal_para_cima()
> > > tv.canal
2"""
class Televisao:
    def __init__(self,min,max):
        self.ligado = False
        self.canal = 1
        self.min = min
        self.max = max
    
    def mudar_para_baixo(self):
        self.canal -=1
        if self.canal < self.min:
            self.canal = self.max
        return self.canal
    def mudar_para_cima(self):
        self.canal +=1
        if self.canal > self.max:
            self.canal = self.min
        return self.canal
tv_da_sala = Televisao(1,30)
tv_quarto = Televisao(1,30)
print(f"canal atual: {tv_da_sala.canal}")
print(f"Para baixo: {tv_da_sala.mudar_para_baixo()}")
print(f"Para cima: {tv_da_sala.mudar_para_cima()}")
    
        