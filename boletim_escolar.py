boletim = {}
boletim['nome'] = input("Digite seu nome: ")
boletim['notas'] = []
nota_para_aprovacao = 5.0

for i in range(3):
    nota = float(input(f"Digite a {i + 1}º nota: "))
    boletim['notas'].append(nota)

media = sum(boletim['notas']) / len(boletim['notas'])

if media >= nota_para_aprovacao:
    print(f"Aprovado! Sua média foi de {media:.2f}.")
else:
    print(f"Reprovado! Sua média foi de {media:.2f}.")
