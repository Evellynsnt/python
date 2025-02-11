for x in range(30):
    print('Evellyn')

print(" ")
print("-------------------------------------------------------------- ")

numeros = [12,25,33,50,11]
for x in range(len(numeros)):
    print(numeros[x])

for x in numeros:
    print(x)

print(" ")
print("-------------------------------------------------------------- ")

numeros = []

while True:
    valor = int(input("Digite um número: "))
    if (valor==-1):
        break
    else:
        numeros.append(valor)

for x in numeros:
    if (x%2==0):
        print(x)
