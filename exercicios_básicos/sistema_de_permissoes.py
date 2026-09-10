print("1-Usuário")
print("2-Moderador")
print("3-Administrador")
permissao = int(input("Digite o número correspondente ao seu nível de permissão: "))

if permissao == 1:
    print("Você logou como usuário.")
elif permissao == 2:
    print("Você logou como moderador.")
elif permissao == 3:
    print("Você logou como administrador.")
else:
    print("Permissão inválida. Tente novamente.")