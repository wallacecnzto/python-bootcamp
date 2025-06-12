preco = float(input("Digite o preço do produto: "))
desconto = preco * (10 / 100)
preco_final = preco - desconto

print(f"O preco do produto é de R$ {preco_final:.2f}")
