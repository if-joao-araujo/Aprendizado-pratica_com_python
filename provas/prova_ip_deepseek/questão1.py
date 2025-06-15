"""
Questão 1 (2,0 pontos)**  
Escreva um programa em Python que:**  
peça ao usuário para digitar dois números inteiros.  
imprima a soma, subtração, multiplicação e divisão entre esses números.  

Exemplo de saída:  
```
Digite o primeiro número: 5  
Digite o segundo número: 3  
Soma: 8  
Subtração: 2  
Multiplicação: 15  
Divisão: 1.666...
```"""
def operacoes(a,b):
  
    return  f"\n soma: {a+b} \n subtração: {a-b}\n multiplicação: {a*b}\n divisão: {a/b}"
   
a = float(input("Digite o numero a: "))
b = float(input("Digite o numero b: "))
print(operacoes(a,b))
