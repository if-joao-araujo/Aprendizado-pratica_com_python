"""São fornecidos os cabeçalhos de duas listas encadeadas classificadas list1e list2.
Mescle as duas listas em uma lista ordenada . A lista deve ser formada juntando os nós 
das duas primeiras listas. Retorna o cabeçalho da lista vinculada mesclada ."""
primeira_lista = [0,7,4,2,9]
segunda_lista = [2,1,3,5,8]
lista = primeira_lista + segunda_lista
lista_ordenada = sorted(lista)
print(lista_ordenada)
#<----> ,-,