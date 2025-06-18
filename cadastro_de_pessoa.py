cadastro = {}

cadastro['nome'] = input("Digite seu nome: ")
cadastro['idade'] = int(input("Digite sua idade: "))
cadastro['cidade'] = input("Digite sua cidade: ")

print()

print(f"{cadastro['nome']}\n{cadastro['idade']}\n{cadastro['cidade'].capitalize()}")

# for chave, valor in cadastro.items():
#     print(f"{chave} : {valor}")
