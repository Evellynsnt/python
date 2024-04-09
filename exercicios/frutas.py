import os

valorMaca: float
valorMorango: float
fruta: str
kilos: float

print("======== MENU ========")
print("Morango: até 5kg = R$2,50 / acima de 5kg = R$2,20")
print("Maça: até 5kg =  R%1,80 / acima de 5kg = R%1,50")

fruta = input("\nQual fruta gostaria de comprar?")
   
kilos = float(input("Quantos kilos gostaria?"))
   
match (fruta):
    case "maça":
        if kilos > 5:
          total = 1.50 * kilos
        else:
          total = 1.80 * kilos
   
    case "morango":
        if kilos > 5:
          total = 2.20 * kilos
        else:
          total = 2.50 * kilos
      

desconto: float
preco: float
total: float

desconto = total * 0.10

if total > 25 or kilos > 8:
    total = preco - desconto
    print(f"O total a ser pago vai ser: {total}")
else: 
    print(f"O valor a ser pago vai ser: {total}")

