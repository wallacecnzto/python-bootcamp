print("CADASTRO DE NOMES")
print()
lista_de_nomes = []
opcao = input("Digite [a] para adicionar ou [s] para sair: ")

while opcao != "s":
    nome = input("Digite um nome: ")
    lista_de_nomes.append(nome)
    opcao = input("Deseja adicionar mais nomes [a]/[s]?")

print()

for i in lista_de_nomes:
    print(i)
