"""Exercício 1 (Fácil): Contagem de Letras
Crie uma função que recebe uma string e retorna um dicionário onde as chaves são 
as letras da string e os valores são a quantidade de vezes que cada letra aparece 
(case-insensitive, ou seja, 'A' e 'a' são a mesma letra).

Exemplo:
Entrada: "Abacaxi"
Saída: {'a': 3, 'b': 1, 'c': 1, 'x': 1, 'i': 1}"""

def cont_vogal(v):
    v= v.lower()
    vogais  = {"a":0,"e":0,"i":0,"o":0,"u":0}
    
    for c in v:
        if c == "a":
           vogais["a"] +=1
        elif c == "e":
            vogais["e"] +=1
        elif c == "i":
            vogais["i"] +=1
        elif c == "o":
            vogais["o"] +=1
        elif c == "u":
            vogais["u"] +=1
        else:
            continue
    return f"---> {vogais}"

v = input("digite alguma paralavra---> ")

print(cont_vogal(v))
