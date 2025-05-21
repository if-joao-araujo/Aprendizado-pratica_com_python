numeros = [num for num in range(1,11) ]
print(numeros)

filmes = ["Piratas do caribe","O lutador","A voz do silencio","minecraft","titanic"]
print(filmes)

assistido = input("qual filme voce assistiu? ")
filmes_assistidos = [filme for filme in filmes if filme != assistido]
print(f"filmes que faltam assistir {filmes_assistidos}")

while True:
   encontrar_filmes = input("Digite o nome do filme, ou ( sair) para sair: ").lower()
   filmes_disponiveis = [buscar_filmes for buscar_filmes in filmes  if encontrar_filmes.lower() in buscar_filmes.lower() ]
   if encontrar_filmes == "sair":
      break

   if filmes_disponiveis:
      print(encontrar_filmes.lower())
      for buscando in filmes_disponiveis:
          if encontrar_filmes in buscando:
             print(f"filmes disponiveis: {buscando}\n")

   else:
      print("filme não encontrado")
 