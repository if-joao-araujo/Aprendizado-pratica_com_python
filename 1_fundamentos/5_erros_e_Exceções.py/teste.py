try:
    a = int(input("digite um numero: "))
    b = int(input("digite outro numero: "))
    r = a/b
except ZeroDivisionError:
     print("não existe divisão por zero")
except (ValueError, TypeError):
    print("tivemos um problema  com os tipos de dados digitados")
except KeyboardInterrupt:
    print("voçe esqueceu de digitar algum dado")
else:
   print(f"O resultado é {r}")
finally:
     print("volte sempre!!")


