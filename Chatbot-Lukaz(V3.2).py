from textblob import TextBlob
import re
import random
print("""Olá Mundo! 
Saudações, eu me chamo Lukaz. Como posso ajudá-lo?""")

def update_pairs():
    global pairs
    pairs = [
    (r'^oi$|^olá$|^Oi$|^Olá$', ['Olá!', 'Oi!']),
    (r'oi Lukaz|Oi Lukaz|olá Lukaz|Olá Lukaz', [f'Olá {UserName}!', f'Oi {UserName}!', f'Como vai, {UserName}?']),
    (r'Saudações|saudações', ['Saudações. Como posso servi-lo?']),
    (r'qual é o seu nome?|Qual é o seu nome?', ['Meu nome é Lukaz.', 'Pode me chamar de Lukaz.']),
    (r'qual é o maior animal terrestre?|Qual é o maior animal terrestre?', ['O maior animal terrestre é o elefante.']),
    (r'qual é o maior animal aquático?|Qual é o maior animal aquático?', ['O maior animal aquático é a baleia-azul que por sinal também é o maior animal existente.']),
    (r'qual é o maior animal existente?|Qual é o maior animal existente', ['O maior animal existente é a baleia-azul.']),
    (r'qual é o maior animal que existe?|Qual é o maior animal que existe?', ['O maior animal que existe é a baleia-azul.']),
    (r'Qual é a capital do Brasil?|qual é a capital do Brasil?', ['A capital do Brasil é Brasília.']),
    (r'Qual é o nome da capital do Brasil?|qual é o nome da capital do Brasil?|Como se chama a capital do Brasil?|como se chama a capital do Brasil?', ['A capital do Brasil se chama Brasília.']),
    (r'qual é o maior animal que existe?|Qual é o maior animal que existe?', ['O maior animal que existe é a baleia-azul.']),
    (r'Qual é a capital da Argentina?|qual é a capital da Argentina?', ['A capital da Argentina é Buenos Aires.']),
    (r'Qual é o nome da capital da Argentina?|qual é o nome da capital da Argentina?|Como se chama a capital da Argentina?|como se chama a capital da Argentina?', ['A capital da Argentina se chama Buenos Aires.']),
    (r'Qual é a capital da França?|qual é a capital da França?', ['A capital da França é Paris.']),
    (r'Qual é o nome da capital da França?|qual é o nome da capital da França?|Como se chama a capital da França?|como se chama a capital da França?', ['A capital da França se chama Paris.']),
    (r'você gosta de música?|Você gosta de música?', ['Sim, adoro música.']),
    (r'E qual música você gosta?|e qual música você gosta?|Qual música você gosta?|qual música você gosta?|E que tipo música você gosta?|e que tipo música você gosta?|Que tipo de música você gosta?|que tipo de música você gosta?', ['Gosto muito de música eletrônica']),
    (r'Vamos jogar Jokenpô?|vamos jogar Jokenpô?|Vamos jogar jokenpô?|vamos jogar jokenpô?|Vamos jogar Jokenpo?|vamos jogar Jokenpo?|Vamos jogar jokenpo?|vamos jogar jokenpo?', [play_jokenpo]),
    (r'Eu quero jogar Jokenpô|eu quero jogar Jokenpô|Eu quero jogar jokenpô|eu quero jogar jokenpô|Eu quero jogar Jokenpo|eu quero jogar Jokenpo|Eu quero jogar jokenpo|eu quero jogar jokenpo', [play_jokenpo]),
    (r'Vou bem|vou bem', ['Que bom! Fico feliz em ouvir isso.']),
    (r'Vou bem e você?|vou bem e você?', ['Estou ótimo e pronto para servi-lo!']),
    (rf'Eu não sou o {UserName}|eu não sou o {UserName}|Eu não sou o {UserName}|eu não sou o {UserName}|Eu não sou {UserName}|eu não sou {UserName}', [nome2]),
    (rf'^Não me chamo {UserName}$|^não me chamo {UserName}$|^Não chamo {UserName}$|^não chamo {UserName}$|^Meu nome não é {UserName}$|^meu nome não é {UserName}$|^Não é {UserName}$|^não é {UserName}$', [nome2]),
    (r'Ótimo|ótimo|', ['Perfeito! Como posso ajudá-lo?']),
]


UserName = "Usuário"
def nome1():
    global UserName
    UserName = input("E o seu?\n")
    update_pairs()
    return "Certo, lhe chamarei de " + UserName + " agora."

def nome2():
    global UserName
    UserName = input("Nesse caso, como devo chamá-lo?\n")
    update_pairs()
    return "Certo, lhe chamarei de " + UserName + " agora."


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
    (r'oi Lukaz|Oi Lukaz|olá Lukaz|Olá Lukaz', [f'Olá {UserName}!', f'Oi {UserName}!', f'Como vai, {UserName}?']),
    (r'Saudações|saudações', ['Saudações. Como posso servi-lo?']),
    (r'qual é o seu nome?|Qual é o seu nome?', ['Meu nome é Lukaz.', 'Pode me chamar de Lukaz.']),
    (r'qual é o maior animal terrestre?|Qual é o maior animal terrestre?', ['O maior animal terrestre é o elefante.']),
    (r'qual é o maior animal aquático?|Qual é o maior animal aquático?', ['O maior animal aquático é a baleia-azul que por sinal também é o maior animal existente.']),
    (r'qual é o maior animal existente?|Qual é o maior animal existente', ['O maior animal existente é a baleia-azul.']),
    (r'qual é o maior animal que existe?|Qual é o maior animal que existe?', ['O maior animal que existe é a baleia-azul.']),
    (r'Qual é a capital do Brasil?|qual é a capital do Brasil?', ['A capital do Brasil é Brasília.']),
    (r'Qual é o nome da capital do Brasil?|qual é o nome da capital do Brasil?|Como se chama a capital do Brasil?|como se chama a capital do Brasil?', ['A capital do Brasil se chama Brasília.']),
    (r'qual é o maior animal que existe?|Qual é o maior animal que existe?', ['O maior animal que existe é a baleia-azul.']),
    (r'Qual é a capital da Argentina?|qual é a capital da Argentina?', ['A capital da Argentina é Buenos Aires.']),
    (r'Qual é o nome da capital da Argentina?|qual é o nome da capital da Argentina?|Como se chama a capital da Argentina?|como se chama a capital da Argentina?', ['A capital da Argentina se chama Buenos Aires.']),
    (r'Qual é a capital da França?|qual é a capital da França?', ['A capital da França é Paris.']),
    (r'Qual é o nome da capital da França?|qual é o nome da capital da França?|Como se chama a capital da França?|como se chama a capital da França?', ['A capital da França se chama Paris.']),
    (r'você gosta de música?|Você gosta de música?', ['Sim, adoro música.']),
    (r'E qual música você gosta?|e qual música você gosta?|Qual música você gosta?|qual música você gosta?|E que tipo música você gosta?|e que tipo música você gosta?|Que tipo de música você gosta?|que tipo de música você gosta?', ['Gosto muito de música eletrônica']),
    (r'Vamos jogar Jokenpô?|vamos jogar Jokenpô?|Vamos jogar jokenpô?|vamos jogar jokenpô?|Vamos jogar Jokenpo?|vamos jogar Jokenpo?|Vamos jogar jokenpo?|vamos jogar jokenpo?', [play_jokenpo]),
    (r'Eu quero jogar Jokenpô|eu quero jogar Jokenpô|Eu quero jogar jokenpô|eu quero jogar jokenpô|Eu quero jogar Jokenpo|eu quero jogar Jokenpo|Eu quero jogar jokenpo|eu quero jogar jokenpo', [play_jokenpo]),
    (r'Vou bem|vou bem', ['Que bom! Fico feliz em ouvir isso.']),
    (r'Vou bem e você?|vou bem e você?', ['Estou ótimo e pronto para servi-lo!']),
    (rf'Eu não sou o {UserName}|eu não sou o {UserName}|Eu não sou o {UserName}|eu não sou o {UserName}|Eu não sou {UserName}|eu não sou {UserName}', [nome2]),
    (rf'^Não me chamo {UserName}$|^não me chamo {UserName}$|^Não chamo {UserName}$|^não chamo {UserName}$|^Meu nome não é {UserName}$|^meu nome não é {UserName}$|^Não é {UserName}$|^não é {UserName}$', [nome2]),
    (r'Ótimo|ótimo|', ['Perfeito! Como posso ajudá-lo?']),
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

    