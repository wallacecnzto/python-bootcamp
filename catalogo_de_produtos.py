catalogo = {}
qtd_de_produtos = 3

for i in range(3):
    produto = input(f"Digite o nome do {i + 1}º produto: ")
    valor = float(input(f"Digite o valor do {i + 1}º produto: "))
    catalogo[produto] = valor

consulta_de_produto = input("Digite o nome do produto para consulta do preço: ")

if catalogo.get(consulta_de_produto) is None:
    print("Produto não encontrado!")
else:
    consulta_de_preco = catalogo.get(consulta_de_produto)
    print(f"O valor do produto é de {consulta_de_preco:.2f}")
