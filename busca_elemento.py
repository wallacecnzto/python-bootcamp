nomes = []
opcao = input("Digite um nome ou [s] para sair: ")

if opcao.isdigit():
    print("Digite apenas nomes!")
    opcao = input("Digite um nome ou [s] para sair: ")

while opcao != "s":
    nomes.append(opcao)
    opcao = input("Digite outro ou [s] para sair: ")

busca_de_nome = input("Qual nome você quer buscar? ")

if nomes.count(busca_de_nome) > 0:
    print(f"{busca_de_nome} está na lista!")
else:
    print("Seu nome não está na lista!")
