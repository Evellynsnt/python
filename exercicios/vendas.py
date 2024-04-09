import os

produto: str
precounitario: float
quantidade: int
totalPagar: float
total: float
desconto: float

produto = input("Insira o produto que deseja?")
quantidade = float(input("Insira a quantidade que deseja:"))
precoUnitario = float(input("Insira o valor do produto: "))

total = quantidade * precoUnitario

if quantidade <= 5:
    desconto = "5%"
    totalPagar = total - 0.05

if quantidade > 5 and quantidade <= 10:
   desconto = "3%"
   totalPagar = total - 0.03

if quantidade > 10:
    desconto = "5%"
    totalPagar = total - 0.05


print(f"Produto: {produto}")
print(f"Quantidade: {quantidade}")
print(f"Preço unitário: {precoUnitario}")
print(f"Total a pagar: {totalPagar}")

