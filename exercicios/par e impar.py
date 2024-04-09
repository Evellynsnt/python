import os

valoresPar: int = 0
valoresImpar: int = 0

valor1 = int(input("Digite o primeiro número:"))
if valor1 % 2 == 0:
    valoresPar = valoresPar + 1
else:
    valoresImpar = valoresImpar + 1

valor2 = int(input("Digite o segundo número:"))
if valor2 % 2 == 0:
    valoresPar = valoresPar + 1
else:
    valoresImpar = valoresImpar + 1

valor3 = int(input("Digite o terceiro número:"))
if valor3 % 2 == 0:
    valoresPar = valoresPar + 1
else:
    valoresImpar = valoresImpar + 1

valor4 = int(input("Digite o quarto número:"))
if valor4 % 2 == 0:
    valoresPar = valoresPar + 1
else:
    valoresImpar = valoresImpar + 1

valor5 = int(input("Digite o quinto número:"))
if valor5 % 2 == 0:
    valoresPar = valoresPar + 1
else:
    valoresImpar = valoresImpar + 1

soma: int
soma = valor1 + valor2 + valor3 + valor4 + valor5


print(f"Soma: {soma}")
print(f"Números pares: {valoresPar}")
print(f"Números impares: {valoresImpar}")