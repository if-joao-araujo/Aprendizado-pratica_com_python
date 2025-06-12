"""Exercício 10.1 Adicione os atributos tamanho e marca à classe 
Televisão. Crie dois objetos Televisão e atribua tamanhos e marcas 
diferentes. Depois, imprima o valor desses atributos de forma a
confirmar a independência dos valores de cada instância (objeto)."""

class Televisao:
    def __init__(self):
        self.canal = 4
        self.ligado =  "Desligado"
        self.marca = "sanssung"
        self.polegadas = 20

tv_sala = Televisao()
tv_quarto = Televisao()
tv_quarto.ligado = "Ligada"
tv_quarto.canal = 2
tv_quarto.marca = "LG"
tv_quarto.polegadas = 40
print(tv_sala.ligado, tv_sala.canal, tv_sala.marca,tv_sala.polegadas)
print(tv_quarto.ligado, tv_quarto.canal, tv_quarto.marca, tv_quarto.polegadas)
