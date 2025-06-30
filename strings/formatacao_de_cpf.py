cpf = input("Digite seu CPF (somente números): ").strip().casefold()
qtd_digitos_cpf = 11

while len(cpf) != qtd_digitos_cpf:
    cpf = input("CPF inválido, digite novamente: ").strip().casefold()

cpf_formatado = cpf[:3] + '.' + cpf[5:]
cpf_formatado = cpf_formatado[:7] + '.' + cpf[6:]
cpf_formatado = cpf_formatado[:11] + '-' + cpf[9:]
print("Seu CPF é {}.".format(cpf_formatado))