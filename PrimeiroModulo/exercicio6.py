#import e usado para puxar um comando da biblioteca 
#random e usado para gerar um numero aleatorio
import random
#def e usado para definir uma função
# a funçao def é usada para criar uma funçao que pode ser usada varias vezes
def gera():
    return random.randint(1, 100)
# def é uma funçao que gera um numero aleatorio entre 1 e 100
def game():
# def é uma funçao que é usada para jogar o jogo
    resposta = gera()
    tentativa = 0
    print("Palpite gerado")

    chute = 0
    while chute != resposta:
        tentativa = tentativa + 1
        chute = int(input("Qual o seu chute: "))
        if chute < resposta:
            print("Errou! é um valor maior que", chute)
        elif chute > resposta:
            print("Errou! É um numero menor que", chute)
        else:
            print("Parabens voce acertou em", tentativa, "tentativas, o numero era: ", resposta)
# enquanto a funçao game for verdadeira, ela vai continuar rodando
while True:
    game()
    