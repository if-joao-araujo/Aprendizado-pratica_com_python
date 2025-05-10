""". Faca uma funcao chamada 'simplifica’ que recebe como parametro o numerador e
o denominador de uma fracao. Esta funcao deve simplificar a fracao recebida 
dividindo o numerador e o denominador pelo maior fator possivel. Por exemplo, a 
fracao 36/60 simplifica para 3/5 dividindo o numerador e o denominador por 12. A
funcao deve modificar as variaveis passadas como parametro. """
def simplifica(a,b):
    resto_divisor = 0
    resto_divisor_a = 0
    resto_divisor_b = 0
    comum = 0

    if a > b:
      while b!=0: 
          resto_divisor = a%b
          comum = resto_divisor
          resto_divisor_a = a/comum
          b = b/comum 
          comum = resto_divisor_a 
          if comum == 0:
             comum = resto_divisor
             print(f"simplificado fica {a} / {b} == {a/resto_divisor_a}/{b/resto_divisor_b}")
          break
    elif  a < b:
        while a!=0:
            resto_divisor = b%a
            if resto_divisor == 0:
                comum = resto_divisor
                print(f"simplificado fica {b} / {a} == {a/comum}/{b/comum}")
            else:
                print(f"""{a} sobre {b} simplificado é igual a--> {b//comum}/""")
        
            break
a = int(input("digite o numero a --> "))   
b = int(input("digite o numero b --> "))          
simplifica(a,b)

#deixar para outro momento