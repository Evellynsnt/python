import os 

#Limpar o terminal.
os.system("cls || clear")

#Solicitando dados para o usuário.
nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade:"))
peso = float(input("Digite o seu peso: "))

#Exibindo resultados do usuario
print("\n==== Exibindo resultados ====")
print(f"Nome: {nome}")
print(f"Idade: {idade}")
print(f"Peso: {peso}")