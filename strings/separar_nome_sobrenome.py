nome_completo = input("Digite seu nome completo: ").strip().casefold()

nome_sobrenome = nome_completo.split(' ')

print(f"Primeiro nome: {nome_sobrenome[0].capitalize()}")
print(f"Último nome: {nome_sobrenome[1].capitalize()}")
