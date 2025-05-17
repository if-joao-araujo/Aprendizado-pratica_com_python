
"""questão (2)
 Faça um programa para o cálculo de uma folha de pagamento, sabendo que existem descontos que
são: (i) do imposto de renda, que depende do salário bruto (conforme tabela abaixo), (ii) 3% para o
Sindicato e (iii) INSS de 10%. O FGTS corresponde a 11% do salário bruto, mas não é descontado (é a
empresa que deposita).
O salário líquido corresponde ao salário bruto menos os descontos. O programa deverá pedir ao
usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.
Desconto do IR;
Salário Bruto até R$ 900,00 (inclusive) – Isento;
Salário Bruto de R$ 1500,00 (inclusive) – desconto de 5%;
Salario bruto até R$ 2500,00 (Inclusive) – desconto de 10%;
Salário bruto acima de R$ 2500 – Desconto de 20%.
Imprima na tela as informações, dispostas conforme o exemplo abaixo. No exemplo, o valor da hora é 5
e a quantidade de horas é 220. (0,5 pontos)"""

hora_trabalhada = float(input("digite a hora trabalhada: "))
dinheiro_hora =   float(input("digite o salario por hora trabalhada: "))
salario_bruto = hora_trabalhada*dinheiro_hora
imposto_renda = 0
sindicato = salario_bruto*0.03
inss = salario_bruto*0.1
fgts = 0.11*salario_bruto

if salario_bruto <= 900:
   imposto_renda = 0
elif salario_bruto <= 1500:
    imposto_renda = salario_bruto*0.05
elif salario_bruto<= 2500:
    imposto_renda = salario_bruto*0.10
else:
    imposto_renda = salario_bruto*0.20
    
salario = salario_bruto-inss-imposto_renda-sindicato
print(f"""salario bruto --> [{salario_bruto}] descontos:
             (1): imposto --> [{imposto_renda}].
             (2): sindicto --> [{sindicato}].
             (3): inss -->[[{inss}].
             (4): fgts --> [{fgts}].
             --> salario liquido: [{salario}]""")
#concluido em 19minutos