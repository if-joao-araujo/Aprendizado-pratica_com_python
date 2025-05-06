"""criar um sitema para uma loja, poderá ser acrescentado mais algum produto, 
remover algum item, ou mostrar algum item"""

produtos = {"celular":1200, "tablet":1450,"fone de ouvido": 25}
opcao = int(input("deseja->\n--> [1] mostrar produtos.\n-->[2] remover produto.\n-->[3] adicionar produto.\n ---> "))
if opcao == 1:
   for x in produtos.items():
      print(x, end=" ")
elif opcao == 2:
     produto = input("qual produto deseja remover: ")
     if produto  in produtos:
        del produtos[produto]
        print(F" {produto} removido com sucesso!")
     else:
        print("produto não encontrado")
elif opcao == 3:
   produto = input("digite o produto que quer adicionar: ")
   produtos[produto] = int(input(f"digite o preço de {produto}: "))  
else:
   print("digite uma opção valida")


print(produtos)