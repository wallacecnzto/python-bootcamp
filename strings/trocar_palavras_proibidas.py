frase = input("Digite uma frase: ").strip().casefold()
palavras_proibidas = ["idiota", "burro", "feio"]

for palavra in palavras_proibidas:
    frase = frase.replace(palavra, '*' * len(palavra))

print(frase)
