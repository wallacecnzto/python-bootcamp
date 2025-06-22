print("CADASTRO DE FUNCIONÁRIOS")
relatorio_de_funcionarios = {}
cpf = int(input("Digite o CPF (somente números): "))
relatorio_de_funcionarios['CPF'] = cpf
relatorio_de_funcionarios['valores'] = {}
relatorio_de_funcionarios['valores']['nome'] = input("Digite o nome do funcionário: ")
relatorio_de_funcionarios['valores']['cargo'] = input("Digite o cargo do funcionário: ")
print()
print("DADOS DO FUNCIONÁRIO")
print(f"NOME: {relatorio_de_funcionarios['valores']['nome']}")
print(f"CARGO: {relatorio_de_funcionarios['valores']['cargo']}")
print(f"CPF: {relatorio_de_funcionarios['CPF']}")