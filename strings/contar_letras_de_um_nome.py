nome_completo = input("Digite seu nome completo: ")
nome_completo = nome_completo.casefold()
nome_completo = nome_completo.replace(' ', '')
ocorrencia_da_letra = nome_completo.count('a')
nome_completo = len(nome_completo)

print("O número de letras sem espaços é de {} caracteres.".format(nome_completo))
print("A ocorrência da letra 'a' aparece {} vezes".format(ocorrencia_da_letra))