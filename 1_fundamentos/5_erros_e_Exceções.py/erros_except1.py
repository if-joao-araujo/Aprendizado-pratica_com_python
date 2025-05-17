"""crie uma função que só terminará quando o usuario digitar os dados
inteiros, reais, strings corretamente nessa ordem."""
cont = 1
while cont <=4:
    if cont ==1:
        try:   
             int = int(input("digite um numero inteiro --> ")) 
             cont +=1
        except:
            print("digite um valor inteiro")
    elif cont ==2:
        try:
           real= float(input("digite um numero real --> "))
           cont +=1
        except:
             print("digite um real")
    elif cont == 3:
        try:       
           string = input("digite string --> ")
           cont +=1
        except:
            print("digite uma string")
    else:
       print(f"inteiro --> {int}\n real --> {real}\n string --> {string}")
       break