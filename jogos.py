import adivinhacao
import forca

print("*********************************")
print("*******Escolha o seu jogo!*******")
print("*********************************")

print("(1) Forca")
print("(2) Adivinhação")

jogo = int(input("Qual o jogo?"))

if jogo == 1:
    print("Jogando forca")
    forca.jogar()
elif jogo == 2:
    print("Jogando adivinhação")
    adivinhacao.jogar()