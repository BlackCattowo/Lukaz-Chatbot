from textblob import TextBlob
import re
import random


def jokenpo():
    variação = input("""Qual variação de Jokenpo você quer jogar?
(0) Tradicional
(1) Pedra-papel-tesoura-lagarto-spock
""")

    if variação.lower() == "0" or variação.lower() == "tradicional":
        escolhas = ["pedra", "papel", "tesoura"]
    elif variação.lower() == "1" or variação.lower() == "pedra-papel-tesoura-lagarto-spock":
        escolhas = ["pedra", "papel", "tesoura", "lagarto", "spock"]
    else:
        return "Essa não é uma opção válida! Tente novamente! XD"

    escolha_pc = random.choice(escolhas)
    escolha_jogador = input(f"Faça sua jogada ({', '.join(escolhas)}): ").lower()

    if escolha_jogador not in escolhas:
        return "Essa não é uma opção válida! Tente novamente! XD"

    resultado = ""
    if escolha_jogador == escolha_pc:
        resultado = "Empate"
    elif (escolha_jogador == "pedra" and escolha_pc in ("tesoura", "lagarto")) or \
            (escolha_jogador == "papel" and escolha_pc in ("pedra", "spock")) or \
            (escolha_jogador == "tesoura" and escolha_pc in ("papel", "lagarto")) or \
            (escolha_jogador == "lagarto" and escolha_pc in ("papel", "spock")) or \
            (escolha_jogador == "spock" and escolha_pc in ("pedra", "tesoura")):
        resultado = f"Você ganhou! Pois eu escolhi {escolha_pc}"
    else:
        resultado = f"Eu ganhei! Pois escolhi {escolha_pc}"

    return f"Jogamos Jokenpo! {resultado}. Foi divertido."


def play_jokenpo():
    return jokenpo()

pairs = [
    (r'oi|olá|Oi|Olá', ['Olá!', 'Oi!', 'Como vai?']),
    (r'qual é o seu nome?|Qual é o seu nome?', ['Meu nome é Lukaz.', 'Pode me chamar de Lukaz.']),
    (r'o que você faz?|O que você faz?', ['Respondo perguntas, converso com as pessoas e ajudo se possível.']),
    (r'você gosta de música?|Você gosta de música?', ['Sim, adoro música.']),
    (r'sair|Sair', ['Até mais!', 'Tchau!', 'Até a próxima.']),
    (r'oi Lukaz', ['Olá Rafael!', 'Oi Rafael!', 'Como vai?']),
    (r'Vamos jogar Jokenpô?|vamos jogar Jokenpô?|Vamos jogar jokenpô?|vamos jogar jokenpô?|Vamos jogar Jokenpo?|vamos jogar Jokenpo?|Vamos jogar jokenpo?|vamos jogar jokenpo?|', [play_jokenpo])
]

chatbot = TextBlob('')
while True:
    user_input = input("Usuário: ")
    if user_input.lower() in ['sair', 'Sair']:
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

    