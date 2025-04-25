"""22. Crie uma func ̧ao que receba como par  ̃ ametro um valor inteiro e gere como saıda n linhas
com pontos de exclamac ̧ao, conforme o exemplo abaixo (para n = 5):  ̃
!
!!
!!!
!!!!
!!!!!"""
def coluninhas(n):
    if n <= 0:
        return "Digite um valor válido que seja maior que zero."
    else:
        for c in range(1, n + 1):  # Começa em 1 para evitar linha vazia
            print(f"---> {'!' * c}")
        return "Fim da impressão."  # Retorno opcional (só para evitar None)

n = int(input("Digite um número: "))
print(coluninhas(n))

#concluido em 23 minutos e 31 segundos