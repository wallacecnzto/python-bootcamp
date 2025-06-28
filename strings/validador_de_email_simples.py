email = input("Digite seu e-mail: ").strip().casefold()

while not '@' in email or not email.endswith(('.br', '.com', '.org')):
    print("Digite um email válido! ")
    email = input("Digite seu e-mail: ").strip().casefold()

print("Seu e-mail é {}.".format(email))
