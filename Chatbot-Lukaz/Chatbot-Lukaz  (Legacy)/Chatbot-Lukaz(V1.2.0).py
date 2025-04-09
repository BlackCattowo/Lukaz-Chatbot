from textblob import TextBlob
import re
import random


def jokenpo():
    print("Claro!")
    variação = input("""Qual variação de Jokenpo você quer jogar?
(0) Tradicional
(1) Pedra-papel-tesoura-lagarto-spock
""")

    if variação.lower() == "0" or variação.lower() == "tradicional":
        escolhas = ["pedra", "papel", "tesoura"]
    elif variação.lower() == "1" or variação.lower() == "pedra-papel-tesoura-lagarto-spock":
        escolhas = ["pedra", "papel", "tesoura", "lagarto", "spock"]
    else:
        print("Essa não é uma opção válida! Tente novamente! XD")
        return

    escolha_pc = random.choice(escolhas)
    escolha_jogador = input(f"Faça sua jogada ({', '.join(escolhas)}): ").lower()

    if escolha_jogador not in escolhas:
        print("Essa não é uma opção válida! Tente novamente! XD")
        return

    print(f"Eu escolhi {escolha_pc}.")
    if escolha_jogador == escolha_pc:
        print("Empate")
    elif (escolha_jogador == "pedra" and escolha_pc in ("tesoura", "lagarto")) or \
            (escolha_jogador == "papel" and escolha_pc in ("pedra", "spock")) or \
            (escolha_jogador == "tesoura" and escolha_pc in ("papel", "lagarto")) or \
            (escolha_jogador == "lagarto" and escolha_pc in ("papel", "spock")) or \
            (escolha_jogador == "spock" and escolha_pc in ("pedra", "tesoura")):
        print("Você ganhou!")
    else:
        print("Eu ganhei!")


pairs = [
    (r'oi|olá', ['Olá!', 'Oi!', 'Como vai?']),
    (r'qual é o seu nome?', ['Meu nome é Lukaz.', 'Pode me chamar de Lukaz.']),
    (r'o que você faz?', ['Respondo perguntas, converso com as pessoas e ajudo se possível.']),
    (r'você gosta de música?', ['Sim, adoro música.']),
    (r'tchau|flw', ['Até mais!', 'Tchau!', 'Até a próxima.']),
    (r'oi Lukaz', ['Olá Rafael!', 'Oi Rafael!', 'Como vai?']),
    (r'Vamos jogar Jokenpô?', [jokenpo])
]

chatbot = TextBlob('')
while True:
    user_input = input("Usuário: ")
    if user_input.lower() in ['tchau', 'flw']:
        print("ChatBot: Até mais!")
        break

    found_match = False
    for pattern, responses in pairs:
        if re.search(pattern, user_input, re.IGNORECASE):
            response = random.choice(responses)
            if callable(response):
                response = response()
            print("ChatBot: " + response)
            found_match = True
            break
    if not found_match:
        print("ChatBot: Não entendi, creio que não fui programado para responder isso.")