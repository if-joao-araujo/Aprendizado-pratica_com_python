class game: #classe principal ~classe pai ou classe generica
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

#subclasse ou classe segundaria ou classe filho
class single_player(game):
   def  __init__(self,nome ="",ano_lancamento = 0, nota = 0, historia = ""):#metodo constutor
       super().__int__(self,nome,ano_lancamento,multiplayer = False, nota = 0)
       self.historia = historia
   def techincal_sheet(self):
       super().techincal_sheet()
       print(f"Enrredo: {self.historia}\n")
       
mult_game = game("need for speed",2002,False,9.1)
mult_game.techincal_sheet()

single = single_player("Five nights ats frids",2015,False,9.9,"Jogo de terror em uma pizzaria")
single.techincal_sheet()
