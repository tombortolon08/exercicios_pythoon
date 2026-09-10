conta_bancaria  = 5437.32
saque = float(input("Digite o valor do saque: "))

if saque <= conta_bancaria:
    print(f"Saque realizado com sucesso!")
    print(f"Novo saldo: R$ {conta_bancaria - saque:.2f}")
else:
    print("Saldo insuficiente para realizar o saque. Tente novamente.")