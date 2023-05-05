from textblob import TextBlob
import re
import random
print("""Olá Mundo! 
Saudações, eu me chamo Lukaz. Como posso ajudá-lo?""")


UserName = "Usuário"
def nome1():
    global UserName
    UserName = input("""E o seu?
""")
    return("Certo, lhe chamarei de " + UserName + " agora.")
def nome2():
    global UserName
    UserName = input("""Nesse caso, como devo chamá-lo?
""")
    return("Certo, lhe chamarei de " + UserName + " agora.")


def play_jokenpo():
    return jokenpo()
def jokenpo():
    variação = input(f"""Lukaz: Claro!

Qual variação de Jokenpo você quer jogar?
(0) Tradicional
(1) Pedra-papel-tesoura-lagarto-spock
{UserName}: """)
    if variação.lower() == "0" or variação.lower() == "tradicional":
        escolhas = ["pedra", "papel", "tesoura"]
    elif variação.lower() == "1" or variação.lower() == "pedra-papel-tesoura-lagarto-spock":
        escolhas = ["pedra", "papel", "tesoura", "lagarto", "spock"]
    else:
        return "Essa não é uma opção válida! Tente novamente."

    escolha_pc = random.choice(escolhas)
    escolha_jogador = input(f"""Faça sua jogada ({', '.join(escolhas)}):
""").lower()

    if escolha_jogador not in escolhas:
        return "Essa não é uma opção válida! Tente novamente."

    resultado = ""
    if escolha_jogador == escolha_pc:
        resultado = f"""
Empate. Também escolhi {escolha_pc}"""

    elif (escolha_jogador == "pedra" and escolha_pc in ("tesoura", "lagarto")) or \
            (escolha_jogador == "papel" and escolha_pc in ("pedra", "spock")) or \
            (escolha_jogador == "tesoura" and escolha_pc in ("papel", "lagarto")) or \
            (escolha_jogador == "lagarto" and escolha_pc in ("papel", "spock")) or \
            (escolha_jogador == "spock" and escolha_pc in ("pedra", "tesoura")):
        resultado = f"""
Você ganhou! Pois eu escolhi {escolha_pc}"""

    else:
        resultado = f"""
eu ganhei! Pois escolhi {escolha_pc}"""
    print(f"{resultado}.")
    return play_again()

def play_again():
    resposta = input("Quer jogar novamente? (sim/não): ")
    if resposta.lower() in ["sim", "s"]:
        return jokenpo()
    elif resposta.lower() in ["não", "nao", "n"]:
        print()
        return "Tudo bem. Isso foi divertido!"
    else:
        print("Resposta inválida!.")
        return play_again()
  

pairs = [
    (r'^oi$|^olá$|^Oi$|^Olá$', ['Olá!', 'Oi!']),
    (r'qual é o seu nome?|Qual é o seu nome?', ['Meu nome é Lukaz.', 'Pode me chamar de Lukaz.']),
    (r'o que você faz?|O que você faz?', ['Respondo perguntas, converso com as pessoas e ajudo se possível.']),
    (r'você gosta de música?|Você gosta de música?', ['Sim, adoro música.']),
    (r'sair|Sair', ['Até mais!', 'Tchau!', 'Até a próxima.']),
    (r'oi Lukaz|Oi Lukaz|olá Lukaz|Olá Lukaz', [f'Olá {UserName}!', f'Oi {UserName}!', f'Como vai, {UserName}?']),
    (r'Vamos jogar Jokenpô?|vamos jogar Jokenpô?|Vamos jogar jokenpô?|vamos jogar jokenpô?|Vamos jogar Jokenpo?|vamos jogar Jokenpo?|Vamos jogar jokenpo?|vamos jogar jokenpo?', [play_jokenpo]),
    (r'Vou bem|vou bem', ['Que bom! Fico feliz em ouvir isso.']),
    (r'Vou bem e você?|vou bem e você?', ['Estou ótimo e pronto para servi-lo!']),
    (rf'Eu não sou o {UserName}|eu não sou o {UserName}|Eu não sou o {UserName}|eu não sou o {UserName}', [nome2]),
    (rf'^Não me chamo {UserName}$|^não me chamo {UserName}$|^Não chamo {UserName}$|^não chamo {UserName}$', [nome2]),
]


chatbot = TextBlob('')
while True:
    user_input = input(f"{UserName}: ")
    if user_input.lower() in ['sair', 'Sair']:
        print("Lukaz: Até mais!")
        break
    found_match = False

    for pattern, responses in pairs:
        if re.search(pattern, user_input, re.IGNORECASE):
            response = random.choice(responses)
            if callable(response):
                response = response()
            print("Lukaz: " + response)
            found_match = True
            break

    if not found_match:
        print("Lukaz: Não entendi, creio que não fui programado para responder isso.")

    