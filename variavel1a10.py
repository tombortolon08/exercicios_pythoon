import random

print("Escolha um número entre 1 e 10.")
pc = random.randint(1, 10)
tentativas = 0

while tentativas < 3:
    tentativas += 1
    palpite = int(input("Digite seu palpite: "))

    if palpite == pc:
        print("Parabéns! Você acertou!")
        restart = input("Gostaria de jogar novamente? (Sim/Nao) ").upper()
        if restart == "SIM": 
                    tentativas = 0
        else:
               print("Obrigado por jogar!")
    break                
    print("Tente novamente.")
    print("Você ainda tem", 3 - tentativas, "tentativas restantes.")
    if tentativas == 3:
        print("Suas tentativas acabaram. O número correto era:", pc)

        restart = input("Gostaria de jogar novamente? (Sim/Nao) ").upper()
        if restart == "SIM": 
            tentativas = 0
        else:
            print("Obrigado por jogar!")
            break