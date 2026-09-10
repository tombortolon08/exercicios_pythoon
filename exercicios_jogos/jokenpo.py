import random

print("Jogo Jokenpo!")
print("Você terá 3 tentativas para jogar contra o computador.")

opcoes = ["Pedra", "Papel", "Tesoura", "Fogo", "Agua"]

tentativas = 0

while tentativas < 3:
    tentativas += 1
    jogador = str(input("Escolha entre Pedra, Papel, Tesoura, Fogo ou Agua: " ).capitalize())

    if jogador not in opcoes:
        print("Escolha errada tente novamente.")
        continue

    pc = random.choice(opcoes)

    print("O computador escolheu:", pc)

    if jogador == pc:
        print("Empate!")
    elif jogador == "Pedra":
        if pc == "Tesoura" or pc == "Fogo":
            print("Você venceu!")
        else:
            print("O seu adversario venceu!")
    elif jogador == "Papel":
        if pc == "Pedra" or pc == "Agua":
            print("Você venceu!")
        else:
            print("O seu adversario venceu!")
    elif jogador == "Tesoura":
        if pc == "Papel" or pc == "Agua":
            print("Você venceu!")
        else:
            print("O seu adversario venceu!")
    elif jogador == "Fogo":
        if pc == "Tesoura" or pc == "Papel":
            print("Você venceu!")
        else:
            print("O seu adversario venceu!")
    elif jogador == "Agua":
        if pc == "Fogo" or pc == "Pedra":
            print("Você venceu!")
        else:
            print("O seu adversario venceu!")

    restart = input("Gostaria de jogar novamente? (Sim/Nao) ").upper()
    print("você ainda tem", 3 - tentativas, "tentativas restantes.")
    if restart != "SIM":
        break