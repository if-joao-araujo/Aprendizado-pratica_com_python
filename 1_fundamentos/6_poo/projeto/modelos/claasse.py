class Biblioteca:
    bibliotecas = []

    def __init__(self,nome):
        self.nome = nome
        self.ativo = False
        Biblioteca.bibliotecas.append(self)

    def __str__(self):
        return self.nome
    
    def listar_bibliotecas():
        for biblioteca in Biblioteca.bibliotecas:
            print(f"nome: {biblioteca.nome} ativo: {biblioteca.ativo} ")

biblioteca_cidade = Biblioteca("Biblioteca jaqueira")
biblioteca_shopping = Biblioteca("Biblioteca do shopping")

print(biblioteca_cidade)
print(biblioteca_shopping)
Biblioteca.listar_bibliotecas()



