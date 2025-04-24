"""6. Faca uma func ̧ao que receba 3 numeros inteiros como par  ́ ametro, representando horas, ˆ
minutos e segundos, e os converta em segundos."""

def coversor_horas(numero1,numero2,numero3):
    sg1 = numero1* 3600 
    sg2 = numero2*60
    sgtotal = sg1+sg2+numero3
    return f"{numero1}h em segundos  ---> {sg1}\n {numero2}m em segundos --> {sg2}\n {numero3}\n os segundos totais ---> {sgtotal}"


numero1 = int(input("digite o numero1 --> "))
numero2 = int(input("digite o numero2 --> "))
numero3 = int(input("digite o numero3 ---> "))
print(coversor_horas(numero1,numero2,numero3))