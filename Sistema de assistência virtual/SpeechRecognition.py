print('testando')

import speech_recognition as sr # Biblioteca que possui toda a Inteligência Artificial necessária para o reconhecimento de voz

import os # Biblioteca que interage com o sistema operacional


#  Função para ouvir e reconhecer a fala
def ouvir_microfone():
    #  Habilita o microfone do usuário
    microfone = sr.Recognizer()

    #  Usando o microfone
    with sr.Microphone() as source:

        #  Chama um algoritmo de redução de ruídos no som
        microfone.adjust_for_ambient_noise(source)

        #  Frase para o usuário dizer algo
        print('Diga alguma coisa: ')

        # Armazena o que foi dito em uma variável
        audio = microfone.listen(source)

    try:

        # Passa a variável para o algoritmo reconhecer os padrões
        frase = microfone.recognize_google(audio,language='pt-BR')

        if 'navegador' in frase:
            os.system("start Chrome.exe")

        elif 'Excel' in frase:
            os.system("start Excel.exe")

        elif 'Word' in frase:
            os.system("start Word.exe")

        #  Retorna a frase pronunciada
        print('Você disse: ' + frase)

    #  Se não reconheceu o padrão de fala, exibe a mensagem
    except sr.UnknownValueError:
        print('Não entendi.')

    return frase

ouvir_microfone()
