import os
import random

sorteado = random.randint(1,100)
contador = contador+1

while True: 
    numero = int(input('Digite um número entre 1-100: '))
   
    if(numero==sorteado):
        os.system('cls')
        print(f"Parabéns você acretou o número em {contador} tentativas")
        break
    elif(numero>sorteado):
        print(f"O númeor é menor!!!!")
    else:
        print(f"O númeor é maior!!!!")


