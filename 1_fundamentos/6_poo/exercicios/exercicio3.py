"""Exercício 2: Classe Retângulo
Crie uma classe Retangulo que:

Recebe no construtor (__init__) os atributos largura e altura (ambos números).

Possui um método calcular_area() que retorna a área do retângulo.

Possui um método calcular_perimetro() que retorna o perímetro.

Crie um objeto e teste os métodos.

Exemplo de solução:"""

class Retangulo:
    def __init__(self,altura,largura):
        self.altura = altura
        self.largura = largura
    
    def perimetro_retangulo(self):
        perimetro = 2*(self.altura + self.largura)
        return perimetro

retangulo = Retangulo(15,20)
print(retangulo.perimetro_retangulo())
