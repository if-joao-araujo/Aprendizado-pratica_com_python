def soma(*num): # adicionei um (*), ou seja um argumento!!
    somador = 0
    for c in num:
        somador += c
    return somador

print(soma(4,8,2,10,10,0))
#muito util quando não sabemos o parametro, ou seja deixa o coigo mais dinamico
print(soma(4,8,2,10,10,60))
print(soma(70))

#kwargs adiciona um (**), ele retorna dicionarios, diferente do args que retonar tupla

def apresntacao(**ola):
    for chave, valor in ola.items():
        print(f"{ chave} - {valor}")

print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
apresntacao(nome="joão pedro",caracteristica= "sou bonito", beleza= "muito bonito") 