import nltk
from nltk.chat.util import Chat, reflections

nltk.download('punkt')

pairs = [
    (r'oi|olá', ['Olá!', 'Oi!', 'Como vai?']),
    (r'qual é o seu nome?', ['Meu nome é Lukaz.', 'Pode me chamar de Lukaz.']),
    (r'o que você faz?', ['Respondo perguntas, converso com as pessoas e ajudo se possível.']),
    (r'você gosta de música?', ['Sim, adoro música.']),
    (r'tchau|flw', ['Até mais!', 'Tchau!', 'Até a próxima.']),
    (r'oi Lukaz', ['Olá Rafael!', 'Oi Rafael!', 'Como vai?']),
    (r'', ['Como posso ajudá-lo, mestre?']),
]


chatbot = Chat(pairs, reflections)
chatbot.converse()
