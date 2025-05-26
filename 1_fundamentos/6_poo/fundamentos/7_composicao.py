class game: #classe principal ~classe pai ou classe generica
    total_games = 0 #variavel de classe
    def __init__(self, nome = "", ano_lancamento = 0,online = False, nota = 0):
        self.nome = nome
        self.ano_lancamento = ano_lancamento
        self.online = online
        self.nota = nota
        self.total_evaluetion = 0
        self.evaluertors = 0

    def __str__(self):
       return f"Jogo:{(self.nome)} "
    
    def techincal_sheet(self):   
        print("## Dados do jogo ##")
        print(f"Nome do jogo: {self.nome}\n Ano de lançamento: {self.ano_lancamento}")
        print(f"O jogo é multiplayer: {self.online}\n avaliações {self.nota}\n")
       
class game_estudio:
    def __init__(self, nome = ""):
        self.nome = nome
        self.games = []

    def add_games(self,game):
        self.games.append(game)

    def evaluete_estudio_quality(self):
        self.total_evaluete = sum(game.note for game in self.games)
        num_games = len(self.games)
        if num_games == 0:
            print(f"o estudio {self.nome} ainda não lançou jogo")
        else:
             avarege_note = total_notas / num_games
             print(f"Nota ")