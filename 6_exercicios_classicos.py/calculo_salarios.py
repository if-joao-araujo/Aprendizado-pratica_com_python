"""5 - Faça um algoritmo que leia o valor do salário mínimo e o valor do salário de
 um usuário, calcule quantos salários mínimos esse 
usuário ganha e imprima na tela o resultado.
 (Base para o Salário mínimo R$ 1.293,20)."""

salario_minimo = 1293.20
salario = float(input("Digite seu salário: "))

if salario <= 0:
    print("Valor inválido! O salário deve ser positivo.")
else:
    quantidade = salario / salario_minimo
    print(f"Você recebe {quantidade:.2f} salários mínimos.")