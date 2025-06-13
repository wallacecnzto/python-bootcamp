senha = int(input("Digite a senha: "))

senha_do_usuario = 123456
tentativas = 1

while tentativas <= 4:
    if senha == senha_do_usuario:
        print("Seja bem vindo ao sistema!")
        break
    else:
        print("Senha errada, tente novamente!")
        tentativas += 1
        senha = int(input("Digite a senha: "))
