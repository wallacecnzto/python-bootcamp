moedas = {
    'Dollar': 5.499,
    'Euro': 6.321,
    'Libra': 7.393
}

valor_em_reais = float(input("Digite o valor em reais para converter: "))
moeda = input("Converter em Dólar, Euro ou Libra (digite [d] [e] ou [l])? ")
moeda.lower()

def converter_moeda(valor_em_reais, moeda):
    if moeda == 'd':
        return valor_em_reais / moedas['Dollar']
    elif moeda == 'e':
        return   valor_em_reais / moedas['Euro']
    elif moeda == 'l':
        return valor_em_reais / moedas['Libra']
    else:
        return None

valor_do_real = converter_moeda(valor_em_reais, moeda)

if valor_do_real is not None:
    print(f"{valor_do_real:.2f}")
else:
    print("Moeda inválida. Por favor, digite apenas [d], [e] ou [l].")