valor = int(input("Digite o valor: "))
cem_reais = 100
cinquenta_reais = 50
vinte_reais = 20
dez_reais = 10
dois_reais = 2

qtd_100 = valor // cem_reais
resto = valor % cem_reais
qtd_50 = resto // cinquenta_reais
resto = resto % cinquenta_reais
qtd_20 = resto // vinte_reais
resto = resto % vinte_reais
qtd_10 = resto // dez_reais
resto = resto % dez_reais
qtd_2 = resto // dois_reais

print(f"Notas de 100: {qtd_100}")
print(f"Notas de 50: {qtd_50}")
print(f"Notas de 20: {qtd_20}")
print(f"Notas de 10: {qtd_10}")
print(f"Notas de 2: {qtd_2}")
