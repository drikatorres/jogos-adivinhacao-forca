import random
def jogar():


    print("*********************************")
    print("***Bem vindo ao jogo da forca!***")
    print("*********************************")

    arquivo = open("palavras.txt", "r")
    palavras = []
    for linha in arquivo:
        linha = linha.strip()
        palavras.index(linha)
    arquivo.close()
    numero = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero].upper()
    letras_acertadas = ["_" for letra in palavra_secreta] #cria um "_" para cada letra em palavra secreta
    enforcou = False
    acertou = False
    erros = 0

    print(letras_acertadas)

    #enquanto não enforcou e não certou (True)
    while (not enforcou and not acertou):
        print("jogando...")
        chute = input("Qual a letra?") #usuário entra com o dado

        #tira os espaços e deixa tudo em maiúsculo
        chute = chute.strip().upper()

        if (chute in palavra_secreta):
            index = 0
            #letra dentro da palavra secreta
            for letra in palavra_secreta:
                if chute.upper() == letra.upper(): #verifica se há a letra dentro da palavra secreta
                    letras_acertadas[index] = letra #substitui no index a letra correspondente
                index += 1
        else:
            erros += 1
            print("Você errou :(. Faltam {} tentativas".format(6-erros))
        enforcou = erros == 6
        acertou = "_" not in letras_acertadas #se "_" não está mais em letras acertadas, pois foi substituído no index
        #pela letra correspondente em seu espaço
        print(letras_acertadas)
    print("Fim do jogo")

if(__name__ == "__main__"):
    jogar()
