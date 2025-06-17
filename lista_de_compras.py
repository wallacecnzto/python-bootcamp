print("LISTA DE COMPRAS")
opcao = input("Digite [a] para adicionar, [r] para remover ou [s] para sair: ")
items = []
item = ""

# Falta concluir sanitização do input do usuário (lição de casa!)

while opcao != 's':
    if opcao == 'a':
        item = input("Digite o nome do item para adicionar: ")
        items.append(item)
    elif opcao == 'r':
        if len(items) == 0:
            print("A lista já está vazia!")
        else:
            item = input("Digite o nome do item para remover: ")
            if item in items:
                items.remove(item)
            else:
                print(f"Item {item} não encontrado!")

    print()

    for i in items:
        print(i)

    print()

    opcao = input("Continuar adicionando, removendo ou deseja sair [a/r/s]? ")

print("Saindo da lista de compras!")
