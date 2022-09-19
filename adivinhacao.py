import random

def jogar():
    print("*********************************")
    print("Bem vindo ao jogo de adivinhação!")
    print("*********************************")

    numero_secreto = random.randrange(1, 101)
    total_de_tentativas = 1
    total_de_tentativas = int(total_de_tentativas)
    pontos = 1000

    print("Qual o nível de dificuldade?")
    print("(1) Fácil")
    print("(2) Médio")
    print("(3) Difícil")

    nivel = int(input("Defina a nível: "))

    if nivel == 1:
        nivel = 20
    if nivel == 2:
        nivel = 10
    if nivel == 3:
        nivel = 5


    while (total_de_tentativas <= nivel):
        print("Tentativa {} de {} ".format(total_de_tentativas, nivel))

        chute = input("Digite o seu número: ")

        chute = int(chute)

        if chute < 1 or chute > 100:
            print("Voce deve digitar um número entre 1 e 100!")
            continue

        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        print("Você digitou ", chute)

        if acertou:
            print("Você acertou e fez {} pontos!".format(pontos))
            break
        else:
            if maior:
                print("Você errou, o seu chute foi maior que o número secreto")
            elif menor:
                print("Você errou, o seu chute foi menor que o número secreto")

            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos
        total_de_tentativas = total_de_tentativas + 1

    print("Fim do jogo o número secreto é ", numero_secreto)

    if (__name__ == "__main__"):
        jogar()


    #dia_ini = 24
    #dia_fim = 28
    #mes = "fevereiro"
    #ano = 2017

    #print("Em {} o Carnaval acontece em ".format(ano), mes, "do dia {} até o dia {}".format(dia_ini,dia_fim))
