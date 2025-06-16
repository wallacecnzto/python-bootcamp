notas = []
nota = 0.0
soma_das_notas = 0
qtd_de_notas = 0
media = 0.0

for i in range(5):
    nota = float(input(f"Digite a {i + 1}º nota: "))
    notas.append(nota)

for nota in notas:
    soma_das_notas += nota
    qtd_de_notas += 1

media = soma_das_notas / qtd_de_notas

print(f"A média das 5 notas é de : {media:.2f}.")
