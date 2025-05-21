filme = {"title" : "piratas do caribe",
         "year":2008,
         "imdb rating":9.8,
         "genere":["action", "comedy"]}

print(filme.items()) #mostra os itens separados por tuplas
print("")
print(filme.values())#mostra os valores
print("")
print(filme)
print("")
print(len(filme))
print("")
print(filme.keys())#mostra apenas as chaves
print("")
print(filme.get("title"))#procura um item no dicionario
print("")
filme["director"] = "fulaniho de tall"
print(filme)
print("")
filme.update({"imdb rating": 9.9})# atualiza o valor de alguma chave do dicionario
print(filme) 
print("")
filme.pop("year") #remove um item do dicionario
print(filme)

