potencia = lambda num: num**2
print(potencia(5))

e_par = lambda num: num%2 == 0 
print(potencia(6), e_par(7))

divisao = lambda a,b: a/b
print(divisao(10,5))

inverte_string = lambda texto: texto[::-1]       
print(inverte_string("ana banana safada"))
filmes = ["Jogos vorazes","o predador","it a coisa"]
nota_filmes = {"jogos vorazes":[8.7,9.2,7.4],
               "o predador ":[8.6,8.2,9.4],
               "it a coisa ":[8.9,9.3,7.6]
               }
nota_media = lambda media: sum(nota_filmes[media]) / len(nota_filmes[media])
print(nota_media("predador"))
