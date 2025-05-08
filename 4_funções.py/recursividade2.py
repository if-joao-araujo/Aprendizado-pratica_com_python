"""3. Escreva uma funcao recursiva que calcule a soma dos primeiros  ̃ n cubos: 
S(n) = 1**3 + 2**3 + ... + n**3"""

def soma_cubo_n(n):
    if n == 1:
        return 1
    else:
        return (n**3) + (soma_cubo_n(n-1))

print(soma_cubo_n(8))