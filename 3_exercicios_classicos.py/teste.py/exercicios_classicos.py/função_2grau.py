def grau_2(x,a,b,c):
    return a*x**2 + b*x+c
    
def grau2 (a,b,c):
    if a == 0:
        return 1
    else:    
        bhaskara = (b**2) - 4*a*c
        if bhaskara <0:
            return "Erro: 'a' não pode ser zero (não é uma equação do segundo grau)."
        else:
            x1 = (-b + bhaskara**0.5)/(2*a)
            x2 = (-b - bhaskara**0.5)/(2*a)
            return x1, x2


        
a = int(input("digite o valor de a --> "))
b = int(input("digite o valor de b --> "))
c = int(input("digite o valor de c --> "))
print(f" A função  é igual a {grau2(a,b,c)}")
