class game:
    def __init__(self, nome = "", ano_lancamento = 0,online = False, nota = 0):
        self.nome = nome
        self.ano_lancamento = ano_lancamento
        self.online = online
        self.nota = nota
        #metodo do construtor, quando eu criar um objeto, ele recebera todos esse parametros.

    def __str__(self): #metodo especial. O (self) referencia algum atributo da classe
       return f"Jogo:{(self.nome)} "
    
game1 = game("minecraft",2007,True,9.6)
game2 = game("Fortinite", 2017,True, 7.8)

print(game1)

print(f"Nome do jogo: {game1.nome}\n Ano de lançamento: {game1.ano_lancamento}")
print(f"O jogo é multiplayer: {game1.online}\n avaliações {game1.nota}\n")
print(game2)
print(f"Nome do jogo: {game2.nome}\n Ano de lançamento: {game2.ano_lancamento}")
print(f"O jogo é multiplayer: {game2.online}\n avaliações {game2.nota}\n")