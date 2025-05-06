def conta_vogal(palavra):
    dic = {"a":0,"e":0,"i":0,"o":0,"u":0}
    for c in palavra:
        if c in dic:
           dic[c] +=1
    return dic

print(conta_vogal("pedreiro"))     
   