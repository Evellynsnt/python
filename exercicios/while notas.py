import os

os.system("cls || clear")

nota = float (input("Digite sua nota:"))
while nota < 0 or nota > 10:
    nota = float (input("Digite sua nota:"))

print(f"\nNota: {nota}")
  
if nota >= 7: 
    print("APROVADO.")
else:
    print("REPROVADO")
