def primo(numero):
    conta_divisor_num = 0
    for c in range(1,numero+1):
        if numero % c == 0:
            conta_divisor_num +=1
    if conta_divisor_num <=2:
        return "é primo"
    else: 
        return "não é primo"

print(primo(3))
 