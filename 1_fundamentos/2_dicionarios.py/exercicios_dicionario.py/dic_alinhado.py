filmes = {"filme 1":{"title" : "piratas do caribe",
         "year":2008,
         "imdb rating":9.8,
         "genere":["action", "comedy"]
         },
         "filme 2":{"title" : "o lutador",
         "year":2012,
         "imdb rating":93 ,
         "genere":["action", "figther"]
         },
         "filme 3":{"title" : "the dark night",
         "year":2009,
         "imdb rating":10,
         "genere":["action", "drama"]}
         }

print(filmes.get("filme 3")) #aqui eu posso buscar o filme, caso não queira mostrar tudo
print("")
filmes["filme 3"]["director"] = "cara tranquilo" #Aqui eu adiciono um nova chave e atribuo valor a ela
print(filmes.get("filme 3"))
print("")
del filmes["filme 3"] #aqui eu removo um item
print(filmes)