moedas = {
    'Dolar': 5.499,
    'Euro': 6.321,
    'Libra': 7.393
}

valor_em_reais = float(input("Digite o valor em reais para converter: "))
moeda = input("Converter em Dólar, Euro ou Libra (digite [d] [e] ou [l])? ")

def converter_moeda(valor_em_reais, moeda):
    valor_convertido = 0
    if moeda == 'd':
        valor_convertido = valor_em_reais / moedas['Dolar']
    elif moeda == 'e':
        valor_convertido = valor_em_reais / moedas['Euro']
    else:
        valor_convertido = valor_em_reais / moedas['Libra']
    return valor_convertido

valor_do_real = converter_moeda(valor_em_reais, moeda)

print(f"{valor_do_real:.2f}")