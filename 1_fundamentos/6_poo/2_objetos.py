class game:
    nome = ""
    ano_lancamento = 0
    online = False
    nota = 0

game1 = game()
print(game1)
game1.nome = "League of legends"
game1.ano_lancamento = "2007"
game1.online = True
game1.nota = 8.9
print(f"Nome do jogo: {game1.nome}\n Ano de lançamento: {game1.ano_lancamento}")
print(f"O jogo é multiplayer: {game1.online}\n avaliações {game1.nota}\n")
#jogo2
game2 = game()
game2.nome = "fortinite"
game2.ano_lancamento = "2017"
game.online = True
game2.nota = 8.6
print(f"Nome do jogo: {game2.nome}\n Ano de lançamento: {game2.ano_lancamento}")
print(f"O jogo é multiplayer: {game2.online}\n avaliações {game2.nota}\n")
#jogo3
game3 = game()
game3.nome = "minecraft"
game3.ano_lancamento = "2009"
game3.online = True
game3.nota = 9.9
print(f"Nome do jogo: {game3.nome}\n Ano de lançamento: {game3.ano_lancamento}")
print(f"O jogo é multiplayer: {game3.online}\n avaliações {game3.nota}")