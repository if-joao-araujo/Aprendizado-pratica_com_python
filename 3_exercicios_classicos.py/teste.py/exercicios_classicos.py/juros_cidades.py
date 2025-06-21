"""24. Uma empresa vende o mesmo produto para quatro diferentes estados. Cada 
estado possui uma taxa diferente de imposto sobre o produto 
(MG 7%; SP 12%; RJ 15%; MS 8%). Faca um programa em que o usuario entre com o 
valor e o estado destino do  ́ produto e o programa retorne o preco final do
produto acrescido do imposto do estado  em que ele sera vendido. Se o estado 
digitado nao for valido, mostrar uma mensagem  ́de erro."""

def imposto(valor,cidade):
    imposto_cidade = {"sp":0.12, "mg":0.07, "rj":0.15, "ms": 0.08}
    if cidade in imposto_cidade.keys():
        return f"o preço do produto com o juros ficou {(valor*imposto_cidade[cidade]) + valor}"
    else:
        return "digite uma cidade valida"

valor = float(input("digite o valor do produto: "))
cidade = input("digite a sigla da cidade [rj],[sp,[mg,[ms] -> ")
print(imposto(valor,cidade))