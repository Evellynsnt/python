import os

loginUsuario: str = "Evellyn"
loginSenha: int = 123

loginUsuario = input("Digite seu login: ")
loginSenha = int(input("Digite sua senha: "))

if loginUsuario == "Evellyn" and loginSenha == 123:
    print("Bem-vindo!") 
else:
    loginUsuario != "Evellyn" and loginSenha != 123
    print("Login e senha inválidos.") 
    