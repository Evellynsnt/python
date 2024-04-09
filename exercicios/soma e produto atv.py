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

if valor1 > maiorValor:
    maiorValor = valor1
else:
    menorValor = valor1

if valor2 > maiorValor:
    maiorValor = valor2
else:
    menorValor = valor2


os.system("cls || clear")    

print(f"====== Exibindo Resultados ======")
print(f"Primeiro valor: {valor1}")
print(f"Segundo valor: {valor2}")
print(f"Média: {media}")
print(f"Soma: {soma}")
print(f"Produto: {produto}")
print(f"Maior número: {maiorValor}")
print(f"Menor número: {menorValor}")
