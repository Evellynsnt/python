import os


nome: str
idade: int
nota1: float
nota2: float
nota3: float
nota4: float

nome = input("Digite seu nome: ")
idade = int (input("Insira sua idade: "))
nota1 = float(input("Digite sua primeira nota: "))
nota2 = float(input("Digite sua segunda nota: "))
nota3 = float(input("Digite sua terceira nota: "))
nota4 = float(input("Digite sua quarta nota: "))

media: float
soma: float

#media = (nota1 + nota2 + nota3 + nota4) / 4
soma = nota1 + nota2 + nota3 + nota4 
media = soma / 4

os.system("cls")

print(f"======== Exibindo Resultados ========")
print(f"Nome: {nome}")
print(f"Idade: {idade}")
print(f"Primeira nota: {nota1}")
print(f"Segunda nota: {nota2}")
print(f"Terceira nota: {nota3}")
print(f"Quarta nota: {nota4}")
print(f"Média: {media}")

if media >= 7:
    print("\nAprovado.")
else: 
    print("Reprovado.")
