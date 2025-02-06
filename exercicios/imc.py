import os

peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura: "))

imc: float
imc = peso/(altura*altura)


if (imc < 18.5):
   categoria = "abaixo do peso"
elif (18.5 <= imc < 24.9):
   categoria = "peso normal"
elif (25.0 <= imc < 29.9):
    categoria = "sobrepeso"
elif (30.0 <= imc < 34.9):
    categoria = "obesidade grau I"
elif (35.0 <= imc < 39.9):
    categoria = "obesidade grau II"
elif (imc >= 40.0):
   categoria = "obesidade grau III"

os.system("cls || clear")

print(f"Peso: {peso}")
print(f"Altura: {altura}")
print(f"IMC: {imc}")
print(f"Categoria: {categoria}")
