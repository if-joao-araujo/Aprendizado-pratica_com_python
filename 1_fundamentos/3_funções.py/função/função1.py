"""Faca uma funcao que receba a data atual (dia, mes e ano em inteiro) e exiba-a na tela ˆ
no formato textual por extenso. Exemplo: Data: 01/01/2000, Imprimir: 1 de janeiro de
2000."""

def data(dia,mes,ano):
    meses = ["janeiro","fervereiro","março","abril","maio","junho",
          "julho","agosta","setembro","outubro","novembro","dezembro"]
   

    print(dia,"de" ,meses[mes-1]," do ano de" ,ano)

dia = int(input("digite o dia: "))
mes = int(input("digite o mes: "))
ano = int(input("digite o ano: "))

data(dia,mes,ano)


  #não cronometrei     
 