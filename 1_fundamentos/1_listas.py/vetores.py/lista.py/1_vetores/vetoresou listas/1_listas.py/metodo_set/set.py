filme = {1,2,3,3,4}
print(filme)

print(len(filme))

teste_set = {"meus bagos",1,True,8.5,0,False}

print(teste_set)#Ele considera 1 = True e 0 = False, Como o set não repete, então ele mostra apenas o 1 
#no lugar do True
filme.update(teste_set)
print(filme) # --> O update junta os set, como tem elementos repetidos, ele só ignora

filme.remove(1)
print(filme) # Eu removi o 1, e de brinde o True foi de comes e bebis

#é parecido com dicionario, por causa das chaves, é tipo 
#uma lista que os elementos repetidos são ignorados