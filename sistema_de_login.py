print("Realize seu cadastro!")
nome_cadastro = input("Digite seu nome: ")
senha_cadastro = int(input("Digite sua senha: "))
print("Cadastro realizado com sucesso!")

login_nome = input("Digite seu nome para login: ")
if login_nome == nome_cadastro:
    login_senha = int(input("Digite sua senha para login: "))
else:
    print("Nome não encontrado. Tente novamente.")

if login_senha == senha_cadastro:
        print("Login realizado com sucesso!")
else:
        print("Senha incorreta. Tente novamente.")