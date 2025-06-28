palavra = input("Digite a palavra: ").strip().casefold()

if palavra[::-1] == palavra:
    print("É palíndromo")
else:
    print("Não é palíndromo!")


