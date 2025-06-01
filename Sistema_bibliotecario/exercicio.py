print("SISTEMA BIBLIOTECARIO")

class Biblioteca:
    def __init__(self,nome,autor,ano,avaliacao):
        self.nome = nome
        self.autor = autor
        self.ano = ano
        self.avaliacao = avaliacao

    def cadastro_livros(self):
        self.livro = {self.nome:{self.autor,self.ano,self.avaliacao}}
        return self.livro



biblioteca = Biblioteca(nome = input("digite o nome do livro: "),autor = input("Digite o nome do autor: "),
ano = int(input("digite o ano de lançamento do livro: ")),avaliacao=float(input("Digite a avaliação  do livro: ")))    

biblioteca.cadastro_livros('hamlet','shakeasper',1600,9.9)
print(biblioteca.cadastro_livros())
