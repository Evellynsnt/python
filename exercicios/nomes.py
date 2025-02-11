nomes = []

while True:
    sequencia = input("Digite um nome: ").lower()
    if sequencia == "exit":
        break
    else:
        nomes.append(sequencia)

    for x in nomes:
        if(x.startswith('a')):
            print(x.capitalize) # botar em maiusculo a inicial independente de como digitarem
            
print('---------------------------------------------')

print("\nNomes com a letra A:")
for sequencia in nomes:
    print(sequencia)
