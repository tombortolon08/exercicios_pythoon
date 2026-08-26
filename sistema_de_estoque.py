produto = "notebook"
preco = 2500.00
quantidade = 10

total = int(input("Digite quantos notebooks deseja comprar: "))

if total <= quantidade:
  compra = total * preco
  print(f"Você comprou {total} notebooks, totalizando R$ {compra:.2f}.")
else:
  print("Quantidade indisponível em estoque. Tente novamente.")