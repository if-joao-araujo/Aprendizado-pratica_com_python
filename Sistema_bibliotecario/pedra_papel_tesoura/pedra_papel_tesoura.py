from random import randint
opcoes = ["pedra","papel","tesoura"]
try:
  mao = int(input("""Digite 
                    [0]: Pedra
                    [1]: Papel
                    [2]: Tesoura
                    --->   """))
  maquina = randint(0,2)
  print(f"Voçe jogou {opcoes[mao]}")
  print(f"A maquina jogou {opcoes[maquina]}")

  if mao ==0:
     if maquina == 1:
        print("A maquina ganhou")
     elif maquina ==2:
        print("Voçe ganhou")
     else:
        print("Empate")
  elif mao ==1:
     if maquina == 2:
        print("A voçe  ganhou")
     elif maquina ==0:
        print("A maquina  ganhou")
     else:
      print("Empate")
  elif mao ==2:
     if maquina ==0:
      print("A maquina ganhou")
     elif maquina ==1:
       print("Voçe  ganhou") 
     else:
       print("Empate")

except:
  print("Digite uma opção valida")
