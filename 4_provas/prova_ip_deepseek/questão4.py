"""
Questão 4 (2,5 pontos)**  
Escreva uma função em Python chamada `contar_vogais` que:**  
Recebe uma string como parâmetro.  
Retorna o número de vogais (a, e, i, o, u) presentes na string, ignorando maiúsculas/minúsculas.  

Exemplo de uso:python
print(contar_vogais("Programação"))  """

def funcao_conta_vogal(palavra):
    conta_vogais = {"A":0,"E":0,"I":0,"O":0,"U":0}
    for vogal in palavra:
        if "a" == vogal:
            conta_vogais["A"] += 1
        if "e" == vogal:
            conta_vogais["E"] += 1
        if "i" == vogal:
            conta_vogais["I"] += 1
        if "o" == vogal:
            conta_vogais["O"] += 1
        if "u" == vogal:
            conta_vogais["U"] +=1
    print(f"palavra digitada: {palavra}. Vogais: \n")
    return (conta_vogais)
palavra = input("Digite uma palavra: ").lower()
        
        
        
