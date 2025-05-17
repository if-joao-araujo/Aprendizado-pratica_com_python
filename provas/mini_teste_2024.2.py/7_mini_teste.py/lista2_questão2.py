
""": Desenvolva um programa para calcular o valor final de uma venda em uma loja de roupas.
O programa deve solicitar o valor da compra e a forma de pagamento. Aplique os seguintes critérios:
Formas de pagamento no cartão e condições:
●​ Em 2x no cartão: valor original sem desconto
●​ Em 3x até 10x no cartão: acréscimo de 5% + 2% por parcela acima de 3x
O programa deve mostrar um resumo da compra conforme exemplo abaixo (0,5 pontos):
Valor da compra: R$ 1000.00
Parcelas no cartão: 5​
Resumo da compra:
Valor original:
 R$ 1000.00
Acréscimo base (5%):
 R$ 50.00
Acréscimo parcelas (4%):
 R$ 40.00
Total de acréscimos:
 R$ 90.00
Valor final:
 R$ 1090.00
Valor das parcelas (5x):
 R$ 218.00"""
def valor_compra(compra,parcela):
    acrescimo = 0
    contador_parcela = 0.02
    if parcela <=2:
        return f"O valor da compra ficou {compra}, não teve acrescimo"
    elif parcela  <=12:
         if parcela==3:
             acrescimo = compra*0.5
             return f"A compra parcelada em 3x ficou {compra+acrescimo}"
         else:
              for c in range(4,parcela):
                  c = 0.02
                  contador_parcela += c
              acrescimo = (0.05*compra) + (contador_parcela*compra)
              return f" acrescimo: {acrescimo}\nAs compra em {parcela}x parcelas ficou: {contador_parcela*compra:.2f} por parcelas\no valor total ficou: {compra+acrescimo:.2f}" 



    
compra = float(input("digite o valor da compra: "))
parcela = int(input("digite as parcelas: "))
print(valor_compra(compra,parcela))

#concluido em 45 minutos, passei 27 minutos procurando igual um maluco o erro, que era o fo c in range, eu estava 
# acrescetando  uma parcela a mais