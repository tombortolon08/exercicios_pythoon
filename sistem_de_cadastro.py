nome  = str(input("Digite seu nome: "))
idade = int(input("Digite sua idade: "))
email = str(input("Digite seu email: "))

if nome =="" or idade <= 0 or email == "":
    print("Cadastro inválido. Tente novamente.")
else:
    print("Cadastro realizado com sucesso!")
    print(f"Nome: {nome}")
    print(f"Idade: {idade}")
    print(f"Email: {email}")