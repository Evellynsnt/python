import os

valor1: int
valor2: int

valor1 = int (input("Digite o primeiro valor: "))
valor2 = int (input("Digite o segundo valor: "))

media: float
soma: float
produto: float

soma = valor1 + valor2
media = soma / 2
produto = valor1 * valor2

menorValor: int
maiorValor: int 

if valor1 > valor2:
    maiorValor = valor1
else:
    maiorValor = valor2

if valor2 < valor1:
    menorValor = valor2
else:
    menorValor = valor1

os.system("cls || clear")    

print(f"====== Exibindo Resultados ======")
print(f"Primeiro valor: {valor1}")
print(f"Segundo valor: {valor2}")
print(f"Média: {media}")
print(f"Soma: {soma}") 
print(f"Produto: {produto}")
print(f"Maior valor: {maiorValor}")
print(f"Menor valor: {menorValor}")

if valor1 == valor2:
    print("Valores iguais.")
else:
    valor1 != valor2
    print("Valores diferentes.")