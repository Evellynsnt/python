import os

os.system("cls || clear")

nome: str
idade: int
peso: float

nome = input("Digite seu nome: ")
idade = int (input("Digite sua idade: "))
peso = float (input("Digite seu peso:"))

print(f"\n==== Exibindo Resultados ====")
print(f"Nome: {nome}")
print(f"Idade: {idade}")
print(f"Peso: {peso:.3f}")

