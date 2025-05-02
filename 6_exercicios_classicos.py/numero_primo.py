"verificar  Números Primos"

def primo(num):
    conta_divisor = 0
    for c in range(1,num+1):
        if num%c == 0:
           conta_divisor +=1
   
    if conta_divisor <= 2:
        return f"{num} é primo"
    else:
        return f"{num} não é primo"

print(primo(7))

#concluido em 8 minutos e 4 segundos