senha = int(input("Digite a senha: "))

senha_do_usuario = 123456
tentativas = 1

while tentativas != 3:
    if senha == senha_do_usuario:
        print("Seja bem vindo ao sistema!")
        break
    else:
        print("Senha errada, tente novamente!")
        print(f"Você só tem mais {3 - tentativas} tentativas!")
        tentativas += 1
        senha = int(input("Digite a senha: "))
