class game:
    total_games = 0 #variavel de classe
    def __init__(self, nome = "", ano_lancamento = 0,online = False, nota = 0):
        self.nome = nome
        self.ano_lancamento = ano_lancamento
        self.online = online
        self.nota = nota
        self.total_evaluetion = 0
        self.evaluertors = 0
        game.total_games +=1

    def __str__(self):
       return f"Jogo:{(self.nome)} "
    
    def techincal_sheet(self):   
        print("## Dados do jogo ##")
        print(f"Nome do jogo: {self.nome}\n Ano de lançamento: {self.ano_lancamento}")
        print(f"O jogo é multiplayer: {self.online}\n avaliações {self.nota}\n")
        
    def evaluete(self,nota):
        self.total_evaluetion += nota
        self.evaluertors +=1
    
    def avarege(self):
        print(f"A média do filme {self.nome} == {self.total_evaluetion / self.evaluertors}")

    
game1 = game("minecraft",2007,True,9.6)
game2 = game("Fortinite", 2017,True, 7.8)
game3 = game("Free fire",2018,True, 8.3)

game1.techincal_sheet()
game1.evaluete(9.0)
game1.evaluete(7.0)
game1.avarege()
game2.evaluete(6)
game2.evaluete(10)
game2.avarege()

print(f"Numero de estancias criadas {game.total_games}")