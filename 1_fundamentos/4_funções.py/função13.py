"""Faca umam funcao que receba a altura e o raio de um cilindro circular e retorne
o volume do cilindro. O volume de um cilindro circular e calculado por meio da 
seguinte formula: V = π ∗ raio2 ∗ altura, onde π = 3.141592."""

def cilindo():
    try:
        pi = 3.141592
        altura = float(input("digite a altura --> "))
        raio = float(input("digite o raio --> "))
        v = pi*(raio**2)*altura
        print(f"o volume é igual a --> {v:.2f}")

    except:
        print("digite apenas numeros!!")
 
   
cilindo()
