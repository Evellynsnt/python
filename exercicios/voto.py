import os 

idade: int 

idade = int(input("Digite sua idade: "))

if idade > 18:
    print("Obrigatório votar.")
if idade < 18 or idade > 65:
    print("Não é obrigtório votar.")


