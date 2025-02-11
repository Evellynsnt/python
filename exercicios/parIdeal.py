import os
import random

nomes = []

for x in range(10):
    n = input((f'Digite um nome do seu crush{x+1}: '))
    nomes.append(n)

crush = random.choice(nomes)

os.system('cls')

print(f'Seu crush ideal é {crush.capitalize()}')
