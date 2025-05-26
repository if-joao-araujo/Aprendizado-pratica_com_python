"""Exercício 1: Classe Pessoa
Crie uma classe Pessoa com os seguintes requisitos:

Atributos: nome (str), idade (int) e altura (float).

Método apresentar() que imprime uma mensagem como:
"Olá, meu nome é [nome], tenho [idade] anos e [altura]m de altura."

Crie um objeto dessa classe e chame o método apresentar()."""
class pessoa:
    def __init__(self, nome, idade, altura):
        self.nome = nome
        self.idade = idade
        self.altura = altura
    def apresentacao(self):
        print(f"Nome {pessoa1.nome}\n idade -> {pessoa1.idade}\n altura -> {pessoa1.altura}") 

pessoa1 = pessoa("Joao pedro",20,1.81)
pessoa1.apresentacao()

