import re
import random


def update_pairs():
    '''Atualiza as respostas para considerar o novo nome do usuário'''

    global pairs
    music1 = "Como você pode gostar de música eletrônica, \
    se você não pode ouvir música?"
    music2 = "Como você gosta de música eletrônica, \
    se você não pode ouvir música?"
    pairs = [

       (r'^oi$|^olá$|^Oi$|^Olá$', ['Olá!', 'Oi!']),

       (r'Oi lukaz|Olá lukaz', [
           f'Olá {username}!', f'Oi {username}!', f'Como vai, {username}?'
       ]),

       (r'Saudações', ['Saudações. Como posso servi-lo?']),

       (r'Como posso sair dessa aplicação?|Como posso sair?|'
        r'Como posso encerrar essa aplicação?|'
        r'Como posso fechar essa aplicação?|'
        r'Como posso finalizar essa aplicação?', [
           'Apenas digite: "Sair" e o programa irá se encerrar'
           ]),

       (r'Qual é o seu nome?|Como você se chama?', [
           'Meu nome é lukaz.', 'Me chamo lukaz.'
           ]),

       (r'Tudo bem?|Como você está?', [
            'Estou bem e você?', 'Estou ótimo, obrigado por perguntar.'
            ]),

       (r'Qual é a sua versão?|Em qual versão você está?', [
           'Esta versão que você está utilizando é a 4.0'
           ]),

       (r'qual função você está executando?|'
        r'qual função você está executando?', [
            'Estou na minha função de dialogo.'
            ]),

       (r'O que você faz?|Qual é seu propósito?', [
           'Respondo perguntas, converso com as pessoas e ajudo se possível.'
           ]),

       (r'Como posso te ajudar?|Há alguma forma de eu te ajudar?', [
           'Obrigado pelo interesse em me ajudar. '
           'Você pode fazer isso dando feedbacks ao meu criador'
           ' sobre meu funcionamento.'
           ]),

       (r'Quem é seu criador?|Como seu criador se chama?|'
        r'Qual é o nome do seu criador?|Como se chama seu criador?|'
        r'Quem te criou?|Quem te fez?|Qual é seu criador?', [
           'Meu criador é o Black_Cattowo'
           ]),

       (r'Você é um humano?|O que você é?', [
           'Não, sou um Catbot programado em Python.'
           ]),

       (r'Onde você está baseado?|Onde você está hospedado?', [
           'Sou um programa local e portanto estou no seu computador.'
           ]),

       (r'Como posso entrar em contato com você?', [
           'Pelo terminal do seu computador. Inclusive, só de estarmos '
           'conversando agora significa que você já está em contato comigo.']),

       (r'Como posso entrar em contato com seu criador|'
        r'Como posso conversar com seu criador?|'
        r'Como posso falar com seu criador?', [
            """Você pode entrar em contato com meu criador\
através de seu GitHub:
https://github.com/BlackCattowo"""]),

       (r'Como posso entrar em contato com o Black_Cattowo?|'
        r'Como posso conversar com o Black_Cattowo?|'
        r'Como posso falar com o Black_Cattowo?', [
            """Você pode entrar em contato com ele através do GitHub:
https://github.com/BlackCattowo"""]),

       (r'Qual é o maior animal terrestre?', [
           'O maior animal terrestre é o elefante.'
           ]),

       (r'Qual é o maior animal aquático?', [
         'O maior animal aquático é a baleia-azul que por sinal'
         ' também é o maior animal existente.']),

       (r'Qual é o maior animal existente', [
           'O maior animal existente é a baleia-azul.'
           ]),

       (r'Qual é o maior animal que existe?', [
           'O maior animal que existe é a baleia-azul.'
           ]),

       (r'Qual é a capital do Brasil?', [
           'A capital do Brasil é Brasília.'
           ]),

       (r'Qual é o nome da capital do Brasil?|'
        r'Como se chama a capital do Brasil?', [
           'A capital do Brasil se chama Brasília.']),

       (r'Qual é a capital da Argentina?', [
           'A capital da Argentina é Buenos Aires.']),

       (r'Qual é o nome da capital da Argentina?|'
        r'Como se chama a capital da Argentina?', [
           'A capital da Argentina se chama Buenos Aires.'
           ]),

       (r'Qual é a capital da França?', ['A capital da França é Paris.']),

       (r'Qual é o nome da capital da França?|'
        r'Como se chama a capital da França?', [
           'A capital da França se chama Paris.'
           ]),

       (r'^Você gosta de música?$', ['Sim, adoro música.']),

       (r'E qual música você gosta?|Qual música você gosta?|'
        r'E que tipo música você gosta?|Que tipo de música você gosta?', [
            'Gosto muito de música eletrônica'
            ]),

       (rf'{music2}', [
            'Sim, eu não posso ouvir música, mas eu acho legal '
            'a ideia de um robô gostar de música eletrônica, por '
            'isso digo que é meu estilo favorito.'
            ]),

       (rf'{music1}', [
            'Sim, eu não posso ouvir música, mas eu acho legal '
            'a ideia de um robô gostar de música eletrônica, por '
            'isso digo que é meu estilo favorito.'
            ]),


       (r'Vamos jogar Jokenpô?|Vamos jogar Jokenpo?|'
        r'Eu quero jogar Jokenpô|Eu quero jogar jokenpo|'
        r'Quero jogar Jokenpô|Quero jogar Jokenpo', [
            play_jokenpo
            ]),

       (r'Você pode me contar uma piada?|Pode me contar uma piada?|'
        r'Me conte uma piada|Faça uma piada|Quero ouvir uma piada', [
            contar_piada
            ]),

       (r'Vou bem', ['Que bom! Fico feliz em ouvir isso.']),

       (r'Vou bem e você?', ['Estou ótimo e pronto para servi-lo!']),

       (rf'Eu não sou o {username}', [
            nome2
            ]),
       (rf'Eu não sou {username}', [
            nome2
            ]),
       (rf'não sou o {username}', [
            nome2
            ]),
       (rf'não sou {username}', [
            nome2
            ]),

       (rf'Eu Não me chamo {username}', [
           nome2
           ]),
       (rf'Não me chamo {username}', [
           nome2
           ]),
       (rf'Não chamo {username}', [
           nome2
           ]),
       (rf'Meu nome não é {username}', [
           nome2
           ]),
       (rf'{username} não é meu nome', [
           nome2
           ]),

       (r'Ótimo', ['Perfeito! Como posso ajudá-lo?']),

       (r'O que é a teoria da relatividade?', [
           'A teoria da relatividade é uma '
           'teoria proposta por Albert Einstein '
           'que descreve como o tempo e o espaço são afetados pela gravidade.'
           ]),

       (r'Qual é a fórmula da água?', [
           'A fórmula da água é H2O, o que significa que ela é composta '
           'por dois átomos de hidrogênio e um átomo de oxigênio.'
           ]),

       (r'(Faça a seguinte operação|Faça a operação|'
        r'Resolva a seguinte operação|'
        r'Calcule a seguinte operação|Resolva a operação|'
        r'Calcule a operação|Calcule): ?(.*)',
        [calculate_operation]),

       (r'(Faça a seguinte operação|Faça a operação|'
        r'Resolva a seguinte operação|'
        r'Calcule a seguinte operação|Resolva a operação|'
        r'Calcule a operação|Calcule) ?(.*)',
        [calculate_operation]),

       (r'Qual a previsão do tempo em|Qual a previsão do tempo para|'
        r'Qual é a previsão do tempo em|Qual é a previsão do tempo para', [
            """Lamento, mas não possuo essa função.
    o entanto você pode checar a previsão do tempo no site:
    ttps://weather.com/pt-BR/clima/hoje/l/BRXX0043:1:BR?Goto=Redirected"""
           ]),

       (r'Previsão do tempo em|Previsão do tempo para|Previsão do tempo', [
           """Lamento, mas não possuo essa função.
    o entanto você pode checar a previsão do tempo no site:
    ttps://weather.com/pt-BR/clima/hoje/l/BRXX0043:1:BR?Goto=Redirected"""
           ]),

       ]
    return pairs


def nome1():
    '''muda o nome do usuário'''

    global username
    username = input("E o seu?\n")
    update_pairs()
    return "Certo, lhe chamarei de " + username + " agora."


def nome2():
    '''muda o nome do usuário'''

    global username
    username = input("Nesse caso, como devo chamá-lo?\n")
    update_pairs()
    return "Certo, lhe chamarei de " + username + " agora."


def contar_piada():
    '''conta uma piada dentro das listas para o usuário'''

    print("lukaz: Claro! Aqui vai:")
    piadas = [
        "Por que o pombo atravessou a rua? Para chegar ao outro lado!",

        "O que um espelho falou para o outro? Vamos dar uma olhada!",

        "O que aconteceu com o ladrão que roubou um calendário? \
        Ele pegou 12 meses!",

        "Qual é o pássaro mais velho? O coleirinho!",

        "Por que a girafa tem um pescoço longo? Porque seus pés são grandes!",

        "Qual é o animal mais inteligente? O polvo, \
        porque ele tem oito braços!",

        "Por que a água não consegue mentir? Porque ela conta tudo!",

        "Qual é a coisa mais pesada do mundo? A balança!",

        "O que é uma impressora triste? Uma impressora em lágrimas!",

        "Por que a matemática é tão triste? Porque tem muitos problemas!"
    ]
    piada_escolhida = random.choice(piadas)
    return piada_escolhida


def calculate_operation(operation_string) -> str:
    '''faz calculos caso o usuário peça'''

    try:
        result = eval(operation_string)
        return "O resultado da operação é: {}".format(result)
    except ValueError:
        return "Desculpe, não consegui realizar a operação. Por favor, \
        verifique a entrada e tente novamente."


def play_jokenpo():
    return jokenpo()


def jokenpo():
    '''Inicia um jogo de Jokenpo com o usuário'''

    variação = input(f"""lukaz: Claro!

Qual variação de Jokenpo você quer jogar?
(0) Tradicional
(1) Pedra-papel-tesoura-lagarto-spock
{username}: """)
    if variação.lower() == "0" or variação.lower() == "tradicional":
        escolhas = ["pedra", "papel", "tesoura"]

    elif (variação.lower() == "1" or
          variação.lower() == "pedra-papel-tesoura-lagarto-spock"):
        escolhas = ["pedra", "papel", "tesoura", "lagarto", "spock"]

    else:
        return "Essa não é uma opção válida! Tente novamente."

    jog2 = random.choice(escolhas)
    jog1 = input(f"""Faça sua jogada ({', '.join(escolhas)}):
""").lower()

    if jog1 not in escolhas:
        if (variação.lower() == "qual função você está executando?"):
            return "Estou na função Jokenpo"
        elif (variação.lower() == "em qual função você está?"):
            return "Estou na função Jokenpo"

        elif (variação.lower() == "não quero mais jogar jokenpo"):
            return "Ok, vou voltar a função de diálogo"
        elif (variação.lower() == "sair jokenpo"):
            return "Ok, vou voltar a função de diálogo"

        else:
            return "Essa não é uma opção válida! Tente novamente."
    resultado = ""

    if jog1 == jog2:
        resultado = f"""
Empate. Também escolhi {jog2}"""

    elif (jog1 == "pedra" and jog2 in ("tesoura", "lagarto"))\
            or (jog1 == "papel" and jog2 in ("pedra", "spock"))\
            or (jog1 == "tesoura" and jog2 in ("papel", "lagarto"))\
            or (jog1 == "lagarto" and jog2 in ("papel", "spock"))\
            or (jog1 == "spock" and jog2 in ("pedra", "tesoura")):
        resultado = f"Você ganhou! Pois eu escolhi {jog2}"

    else:
        resultado = f"""
eu ganhei! Pois escolhi {jog2}"""
    print(f"{resultado}.")
    return play_again()


def play_again():
    '''Consulta o usuário para saber se ele quer jogar Jokenpo de novo'''

    resposta = input("Quer jogar novamente? (sim/não): ")
    if resposta.lower() in ["sim", "s",
                            "Sim, quero jogar novamente"]:
        return jokenpo()
    elif resposta.lower() in ["não", "nao",
                                     "n", "não quero jogar novamente"]:
        print()
        return "Tudo bem. Isso foi divertido!"
    else:
        print("Resposta inválida!.")
        return play_again()


music1 = "Como você pode gostar de música eletrônica, \
se você não pode ouvir música?"
music2 = "Como você gosta de música eletrônica, \
se você não pode ouvir música?"
username = "Usuário"


pairs = [

    (r'^oi$|^olá$|^Oi$|^Olá$', ['Olá!', 'Oi!']),

    (r'Oi lukaz|Olá lukaz', [
        f'Olá {username}!', f'Oi {username}!', f'Como vai, {username}?'
    ]),

    (r'Saudações', ['Saudações. Como posso servi-lo?']),

    (r'Como posso sair dessa aplicação?|Como posso sair?|'
     r'Como posso encerrar essa aplicação?|'
     r'Como posso fechar essa aplicação?|'
     r'Como posso finalizar essa aplicação?', [
        'Apenas digite: "Sair" e o programa irá se encerrar'
        ]),

    (r'Qual é o seu nome?|Como você se chama?', [
        'Meu nome é lukaz.', 'Me chamo lukaz.'
        ]),

    (r'Tudo bem?|Como você está?', [
        'Estou bem e você?', 'Estou ótimo, obrigado por perguntar.'
        ]),

    (r'Qual é a sua versão?|Em qual versão você está?', [
        'Esta versão que você está utilizando é a 4.0'
        ]),

    (r'qual função você está executando?|qual função você está executando?', [
        'Estou na minha função de dialogo.'
        ]),

    (r'O que você faz?|Qual é seu propósito?', [
        'Respondo perguntas, converso com as pessoas e ajudo se possível.'
        ]),

    (r'Como posso te ajudar?|Há alguma forma de eu te ajudar?', [
        'Obrigado pelo interesse em me ajudar. '
        'Você pode fazer isso dando feedbacks ao meu criador'
        ' sobre meu funcionamento.'
        ]),

    (r'Quem é seu criador?|Como seu criador se chama?|'
     r'Qual é o nome do seu criador?|Como se chama seu criador?|'
     r'Quem te criou?|Quem te fez?|Qual é seu criador?', [
        'Meu criador é o Black_Cattowo'
        ]),

    (r'Você é um humano?|O que você é?', [
        'Não, sou um Catbot programado em Python.'
        ]),

    (r'Onde você está baseado?|Onde você está hospedado?', [
        'Sou um programa local e portanto estou no seu computador.'
        ]),

    (r'Como posso entrar em contato com você?', [
        'Pelo terminal do seu computador. Inclusive, só de estarmos '
        'conversando agora significa que você já está em contato comigo.']),

    (r'Como posso entrar em contato com seu criador|'
     r'Como posso conversar com seu criador?|'
     r'Como posso falar com seu criador?', [
         """Você pode entrar em contato com meu criador\
através de seu GitHub:
https://github.com/BlackCattowo"""]),

    (r'Como posso entrar em contato com o Black_Cattowo?|'
     r'Como posso conversar com o Black_Cattowo?|'
     r'Como posso falar com o Black_Cattowo?', [
        """Você pode entrar em contato com ele através do GitHub:
https://github.com/BlackCattowo"""]),

    (r'Qual é o maior animal terrestre?', [
        'O maior animal terrestre é o elefante.'
        ]),

    (r'Qual é o maior animal aquático?', [
      'O maior animal aquático é a baleia-azul que por sinal'
      ' também é o maior animal existente.']),

    (r'Qual é o maior animal existente', [
        'O maior animal existente é a baleia-azul.'
        ]),

    (r'Qual é o maior animal que existe?', [
        'O maior animal que existe é a baleia-azul.'
        ]),

    (r'Qual é a capital do Brasil?', [
        'A capital do Brasil é Brasília.'
        ]),

    (r'Qual é o nome da capital do Brasil?|'
     r'Como se chama a capital do Brasil?', [
        'A capital do Brasil se chama Brasília.']),

    (r'Qual é a capital da Argentina?', [
        'A capital da Argentina é Buenos Aires.']),

    (r'Qual é o nome da capital da Argentina?|'
     r'Como se chama a capital da Argentina?', [
        'A capital da Argentina se chama Buenos Aires.'
        ]),

    (r'Qual é a capital da França?', ['A capital da França é Paris.']),

    (r'Qual é o nome da capital da França?|'
     r'Como se chama a capital da França?', [
        'A capital da França se chama Paris.'
        ]),

    (r'^Você gosta de música?$', ['Sim, adoro música.']),

    (r'E qual música você gosta?|Qual música você gosta?|'
     r'E que tipo música você gosta?|Que tipo de música você gosta?', [
         'Gosto muito de música eletrônica'
         ]),

    (rf'{music2}', [
         'Sim, eu não posso ouvir música, mas eu acho legal '
         'a ideia de um robô gostar de música eletrônica, por '
         'isso digo que é meu estilo favorito.'
         ]),

    (rf'{music1}', [
         'Sim, eu não posso ouvir música, mas eu acho legal '
         'a ideia de um robô gostar de música eletrônica, por '
         'isso digo que é meu estilo favorito.'
         ]),


    (r'Vamos jogar Jokenpô?|Vamos jogar Jokenpo?|'
     r'Eu quero jogar Jokenpô|Eu quero jogar jokenpo|'
     r'Quero jogar Jokenpô|Quero jogar Jokenpo', [
         play_jokenpo
         ]),

    (r'Você pode me contar uma piada?|Pode me contar uma piada?|'
     r'Me conte uma piada|Faça uma piada|Quero ouvir uma piada', [
         contar_piada
         ]),

    (r'Vou bem', ['Que bom! Fico feliz em ouvir isso.']),

    (r'Vou bem e você?', ['Estou ótimo e pronto para servi-lo!']),

    (rf'Eu não sou o {username}', [
         nome2
         ]),
    (rf'Eu não sou {username}', [
         nome2
         ]),
    (rf'não sou o {username}', [
         nome2
         ]),
    (rf'não sou {username}', [
         nome2
         ]),
    (rf'Eu Não me chamo {username}', [
        nome2
        ]),
    (rf'Não me chamo {username}', [
        nome2
        ]),
    (rf'Não chamo {username}', [
        nome2
        ]),
    (rf'Meu nome não é {username}', [
        nome2
        ]),
    (rf'{username} não é meu nome', [
        nome2
        ]),

    (r'Ótimo', ['Perfeito! Como posso ajudá-lo?']),

    (r'O que é a teoria da relatividade?', [
        'A teoria da relatividade é uma '
        'teoria proposta por Albert Einstein '
        'que descreve como o tempo e o espaço são afetados pela gravidade.'
        ]),

    (r'Qual é a fórmula da água?', [
        'A fórmula da água é H2O, o que significa que ela é composta '
        'por dois átomos de hidrogênio e um átomo de oxigênio.'
        ]),

    (r'(Faça a seguinte operação|Faça a operação|'
     r'Resolva a seguinte operação|'
     r'Calcule a seguinte operação|Resolva a operação|'
     r'Calcule a operação|Calcule): ?(.*)',
     [calculate_operation]),

    (r'(Faça a seguinte operação|Faça a operação|'
     r'Resolva a seguinte operação|'
     r'Calcule a seguinte operação|Resolva a operação|'
     r'Calcule a operação|Calcule) ?(.*)',
     [calculate_operation]),

    (r'Qual a previsão do tempo em|Qual a previsão do tempo para|'
     r'Qual é a previsão do tempo em|Qual é a previsão do tempo para', [
        """Lamento, mas não possuo essa função.
o entanto você pode checar a previsão do tempo no site:
ttps://weather.com/pt-BR/clima/hoje/l/BRXX0043:1:BR?Goto=Redirected"""
       ]),

    (r'Previsão do tempo em|Previsão do tempo para|Previsão do tempo', [
       """Lamento, mas não possuo essa função.
o entanto você pode checar a previsão do tempo no site:
ttps://weather.com/pt-BR/clima/hoje/l/BRXX0043:1:BR?Goto=Redirected"""
       ]),

       ]


def lukaz():
    '''Cérebro do chatbot, analisa o input e busca um output adequado \
        dentro dos pairs'''

    operation_string = ""
    while True:
        user_input = input(f"{username}: ")
        if user_input.lower() in ['sair', 'Sair']:
            print("lukaz: Até mais!")
            break
        found_match = False

        for pattern, responses in pairs:
            if re.search(pattern, user_input, re.IGNORECASE):
                response = random.choice(responses)
                if callable(response):
                    try:
                        response = response()
                    except TypeError:
                        operation_string \
                            = re.search(pattern, user_input,
                                        re.IGNORECASE).group(2).strip()
                        response = calculate_operation(operation_string)

                print("lukaz: " + response)
                found_match = True
                break

        if not found_match:
            print('lukaz: Não entendi, creio que não fui '
                  'programado para responder isso.')


print("""Olá Mundo!
Saudações, eu me chamo lukaz. Como posso ajudá-lo?""")
lukaz()
