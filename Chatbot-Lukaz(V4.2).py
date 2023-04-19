from textblob import TextBlob
import re
import random


def update_pairs():
    global pairs
    pairs = [
    (r'^oi$|^olá$|^Oi$|^Olá$', ['Olá!', 'Oi!']),
    (r'Oi Lukaz|Olá Lukaz', [f'Olá {UserName}!', f'Oi {UserName}!', f'Como vai, {UserName}?']),
    (r'Saudações', ['Saudações. Como posso servi-lo?']),
    (r'Como posso sair dessa aplicação?|Como posso sair?|Como posso encerrar essa aplicação?|Como posso fechar essa aplicação?|Como posso finalizar essa aplicação?', ['Apenas digite: "Sair" e o programa irá se encerrar']),
    (r'Qual é o seu nome?|Como você se chama?', ['Meu nome é Lukaz.', 'Me chamo Lukaz.']),
    (r'Qual é a sua versão?|Em qual versão você está?', ['Esta versão que você está utilizando é a 4.0']),
    (r'O que você faz?|Qual é seu propósito?', ['Respondo perguntas, converso com as pessoas e ajudo se possível.']),
    (r'Como posso te ajudar?|Há alguma forma de eu te ajudar?', ['Obrigado pelo interesse em me ajudar. Você pode fazer isso dando feedbacks ao meu criador sobre meu funcionamento.']),
    (r'Quem é seu criador?|Como seu criador se chama?|Qual é o nome do seu criador?|Como se chama seu criador?|Quem te criou?|Quem te fez?|Qual é seu criador?', ['Meu criador é o Black_Cattowo']),
    (r'Você é um humano?|O que você é?', ['Não, sou um Catbot programado em Python.']),
    (r'Onde você está baseado?|Onde você está hospedado?', ['Sou um programa local e portanto estou no seu computador.']),
    (r'Como posso entrar em contato com você?', ['Pelo terminal do seu computador. Inclusive, só de estarmos conversando agora significa que você já está em contato comigo.']),
    (r'Como posso entrar em contato com seu criador|Como posso conversar com seu criador?|Como posso falar com seu criador?', ["""Você pode entrar em contato com meu criador através de seu GitHub:
    https://github.com/BlackCattowo"""]),
    (r'Como posso entrar em contato com o Black_Cattowo?|Como posso conversar com o Black_Cattowo?|Como posso falar com o Black_Cattowo?', ["""Você pode entrar em contato com ele através do GitHub:
    https://github.com/BlackCattowo"""]),
    (r'Qual é o maior animal terrestre?', ['O maior animal terrestre é o elefante.']),
    (r'Qual é o maior animal aquático?', ['O maior animal aquático é a baleia-azul que por sinal também é o maior animal existente.']),
    (r'Qual é o maior animal existente', ['O maior animal existente é a baleia-azul.']),
    (r'Qual é o maior animal que existe?', ['O maior animal que existe é a baleia-azul.']),
    (r'Qual é a capital do Brasil?', ['A capital do Brasil é Brasília.']),
    (r'Qual é o nome da capital do Brasil?|Como se chama a capital do Brasil?', ['A capital do Brasil se chama Brasília.']),
    (r'Qual é a capital da Argentina?', ['A capital da Argentina é Buenos Aires.']),
    (r'Qual é o nome da capital da Argentina?|Como se chama a capital da Argentina?', ['A capital da Argentina se chama Buenos Aires.']),
    (r'Qual é a capital da França?', ['A capital da França é Paris.']),
    (r'Qual é o nome da capital da França?|Como se chama a capital da França?', ['A capital da França se chama Paris.']),
    (r'Você gosta de música?', ['Sim, adoro música.']),
    (r'E qual música você gosta?|Qual música você gosta?|E que tipo música você gosta?|Que tipo de música você gosta?', ['Gosto muito de música eletrônica']),
    (r'Como você pode gostar de música eletrônica, se você não pode ouvir música?|Como você gosta de música eletrônica, se você não pode ouvir música?', ['Sim, eu não posso ouvir música, mas eu acho legal a ideia de um robô gostar de música eletrônica, por isso digo que é meu estilo favorito.']),
    (r'Vamos jogar Jokenpô?|Vamos jogar Jokenpo?|Eu quero jogar Jokenpô|Eu quero jogar jokenpo|Quero jogar Jokenpô|Quero jogar Jokenpo', [play_jokenpo]),
    (r'Você pode me contar uma piada?|Pode me contar uma piada?|Me conte uma piada|Faça uma piada|Quero ouvir uma piada', [contar_piada]),
    (r'Vou bem', ['Que bom! Fico feliz em ouvir isso.']),
    (r'Vou bem e você?', ['Estou ótimo e pronto para servi-lo!']),
    (rf'Eu não sou o {UserName}|Eu não sou {UserName}|não sou o {UserName}|não sou {UserName}', [nome2]),
    (rf'Eu Não me chamo {UserName}|Não me chamo {UserName}|Não chamo {UserName}|Meu nome não é {UserName}|{UserName} não é meu nome', [nome2]),
    (r'Ótimo', ['Perfeito! Como posso ajudá-lo?']),
    (r'O que é a teoria da relatividade?', ['A teoria da relatividade é uma teoria proposta por Albert Einstein que descreve como o tempo e o espaço são afetados pela gravidade.']),
    (r'Qual é a fórmula da água?', ['A fórmula da água é H2O, o que significa que ela é composta por dois átomos de hidrogênio e um átomo de oxigênio.']),
    (r'(Faça a seguinte operação|Faça a operação|Resolva a seguinte operação|Resolva a operação|Calcule a seguinte operação|Calcule a operação|Calcule): ?(.*)', [calculate_operation]),
    (r'(Faça a seguinte operação|Faça a operação|Resolva a seguinte operação|Resolva a operação|Calcule a seguinte operação|Calcule a operação|Calcule) ?(.*)', [calculate_operation]),
    (r'Qual a previsão do tempo em|Qual a previsão do tempo para|Qual é a previsão do tempo em|Qual é a previsão do tempo para', ["""Lamento, mas não possuo essa função. No entanto você pode checar a previsão do tempo no site:
https://weather.com/pt-BR/clima/hoje/l/BRXX0043:1:BR?Goto=Redirected"""]),
    (r'Previsão do tempo em|Previsão do tempo para|Previsão do tempo', ["""Lamento, mas não possuo essa função. No entanto você pode checar a previsão do tempo no site:
https://weather.com/pt-BR/clima/hoje/l/BRXX0043:1:BR?Goto=Redirected"""]),
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


def contar_piada():
    print("Lukaz: Claro! Aqui vai:")
    piadas = [
        "Por que o pombo atravessou a rua? Para chegar ao outro lado!",
        "O que um espelho falou para o outro? Vamos dar uma olhada!",
        "O que aconteceu com o ladrão que roubou um calendário? Ele pegou 12 meses!",
        "Qual é o pássaro mais velho? O coleirinho!",
        "Por que a girafa tem um pescoço longo? Porque seus pés são grandes!",
        "Qual é o animal mais inteligente? O polvo, porque ele tem oito braços!",
        "Por que a água não consegue mentir? Porque ela conta tudo!",
        "Qual é a coisa mais pesada do mundo? A balança!",
        "O que é uma impressora triste? Uma impressora em lágrimas!",
        "Por que a matemática é tão triste? Porque tem muitos problemas!"
    ]
    piada_escolhida = random.choice(piadas)
    return piada_escolhida


def calculate_operation(operation_string):
    try:
        result = eval(operation_string)
        return "O resultado da operação é: {}".format(result)
    except:
        return "Desculpe, não consegui realizar a operação. Por favor, verifique a entrada e tente novamente."    


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
    (r'Oi Lukaz|Olá Lukaz', [f'Olá {UserName}!', f'Oi {UserName}!', f'Como vai, {UserName}?']),
    (r'Saudações', ['Saudações. Como posso servi-lo?']),
    (r'Como posso sair dessa aplicação?|Como posso sair?|Como posso encerrar essa aplicação?|Como posso fechar essa aplicação?|Como posso finalizar essa aplicação?', ['Apenas digite: "Sair" e o programa irá se encerrar']),
    (r'Qual é o seu nome?|Como você se chama?', ['Meu nome é Lukaz.', 'Me chamo Lukaz.']),
    (r'Qual é a sua versão?|Em qual versão você está?', ['Esta versão que você está utilizando é a 4.0']),
    (r'O que você faz?|Qual é seu propósito?', ['Respondo perguntas, converso com as pessoas e ajudo se possível.']),
    (r'Como posso te ajudar?|Há alguma forma de eu te ajudar?', ['Obrigado pelo interesse em me ajudar. Você pode fazer isso dando feedbacks ao meu criador sobre meu funcionamento.']),
    (r'Quem é seu criador?|Como seu criador se chama?|Qual é o nome do seu criador?|Como se chama seu criador?|Quem te criou?|Quem te fez?|Qual é seu criador?', ['Meu criador é o Black_Cattowo']),
    (r'Você é um humano?|O que você é?', ['Não, sou um Catbot programado em Python.']),
    (r'Onde você está baseado?|Onde você está hospedado?', ['Sou um programa local e portanto estou no seu computador.']),
    (r'Como posso entrar em contato com você?', ['Pelo terminal do seu computador. Inclusive, só de estarmos conversando agora significa que você já está em contato comigo.']),
    (r'Como posso entrar em contato com seu criador|Como posso conversar com seu criador?|Como posso falar com seu criador?', ["""Você pode entrar em contato com meu criador através de seu GitHub:
    https://github.com/BlackCattowo"""]),
    (r'Como posso entrar em contato com o Black_Cattowo?|Como posso conversar com o Black_Cattowo?|Como posso falar com o Black_Cattowo?', ["""Você pode entrar em contato com ele através do GitHub:
    https://github.com/BlackCattowo"""]),
    (r'Qual é o maior animal terrestre?', ['O maior animal terrestre é o elefante.']),
    (r'Qual é o maior animal aquático?', ['O maior animal aquático é a baleia-azul que por sinal também é o maior animal existente.']),
    (r'Qual é o maior animal existente', ['O maior animal existente é a baleia-azul.']),
    (r'Qual é o maior animal que existe?', ['O maior animal que existe é a baleia-azul.']),
    (r'Qual é a capital do Brasil?', ['A capital do Brasil é Brasília.']),
    (r'Qual é o nome da capital do Brasil?|Como se chama a capital do Brasil?', ['A capital do Brasil se chama Brasília.']),
    (r'Qual é a capital da Argentina?', ['A capital da Argentina é Buenos Aires.']),
    (r'Qual é o nome da capital da Argentina?|Como se chama a capital da Argentina?', ['A capital da Argentina se chama Buenos Aires.']),
    (r'Qual é a capital da França?', ['A capital da França é Paris.']),
    (r'Qual é o nome da capital da França?|Como se chama a capital da França?', ['A capital da França se chama Paris.']),
    (r'Você gosta de música?', ['Sim, adoro música.']),
    (r'E qual música você gosta?|Qual música você gosta?|E que tipo música você gosta?|Que tipo de música você gosta?', ['Gosto muito de música eletrônica']),
    (r'Como você pode gostar de música eletrônica, se você não pode ouvir música?|Como você gosta de música eletrônica, se você não pode ouvir música?', ['Sim, eu não posso ouvir música, mas eu acho legal a ideia de um robô gostar de música eletrônica, por isso digo que é meu estilo favorito.']),
    (r'Vamos jogar Jokenpô?|Vamos jogar Jokenpo?|Eu quero jogar Jokenpô|Eu quero jogar jokenpo|Quero jogar Jokenpô|Quero jogar Jokenpo', [play_jokenpo]),
    (r'Você pode me contar uma piada?|Pode me contar uma piada?|Me conte uma piada|Faça uma piada|Quero ouvir uma piada', [contar_piada]),
    (r'Vou bem', ['Que bom! Fico feliz em ouvir isso.']),
    (r'Vou bem e você?', ['Estou ótimo e pronto para servi-lo!']),
    (rf'Eu não sou o {UserName}|Eu não sou {UserName}|não sou o {UserName}|não sou {UserName}', [nome2]),
    (rf'Eu Não me chamo {UserName}|Não me chamo {UserName}|Não chamo {UserName}|Meu nome não é {UserName}|{UserName} não é meu nome', [nome2]),
    (r'Ótimo', ['Perfeito! Como posso ajudá-lo?']),
    (r'O que é a teoria da relatividade?', ['A teoria da relatividade é uma teoria proposta por Albert Einstein que descreve como o tempo e o espaço são afetados pela gravidade.']),
    (r'Qual é a fórmula da água?', ['A fórmula da água é H2O, o que significa que ela é composta por dois átomos de hidrogênio e um átomo de oxigênio.']),
    (r'(Faça a seguinte operação|Faça a operação|Resolva a seguinte operação|Resolva a operação|Calcule a seguinte operação|Calcule a operação|Calcule): ?(.*)', [calculate_operation]),
    (r'(Faça a seguinte operação|Faça a operação|Resolva a seguinte operação|Resolva a operação|Calcule a seguinte operação|Calcule a operação|Calcule) ?(.*)', [calculate_operation]),
    (r'Qual a previsão do tempo em|Qual a previsão do tempo para|Qual é a previsão do tempo em|Qual é a previsão do tempo para', ["""Lamento, mas não possuo essa função. No entanto você pode checar a previsão do tempo no site:
https://weather.com/pt-BR/clima/hoje/l/BRXX0043:1:BR?Goto=Redirected"""]),
    (r'Previsão do tempo em|Previsão do tempo para|Previsão do tempo', ["""Lamento, mas não possuo essa função. No entanto você pode checar a previsão do tempo no site:
https://weather.com/pt-BR/clima/hoje/l/BRXX0043:1:BR?Goto=Redirected"""]),
]


def Lukaz():
    chatbot = TextBlob('')
    operation_string = "" 
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
                    try:
                        response = response()
                    except:
                        operation_string = re.search(pattern, user_input, re.IGNORECASE).group(2).strip()
                        response = calculate_operation(operation_string)

                print("Lukaz: " + response)
                found_match = True
                break

        if not found_match:
            print("Lukaz: Não entendi, creio que não fui programado para responder isso.")


print("""Olá Mundo! 
Saudações, eu me chamo Lukaz. Como posso ajudá-lo?""")
Lukaz()

        

