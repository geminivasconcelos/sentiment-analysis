from textblob import TextBlob
from googletrans import Translator
import nltk
import requests

# Baixar recursos do NLTK
nltk.download('vader_lexicon')


# Criar uma função para análise de sentimento
def analisar_sentimento(texto):
    '''
    Função para realizar análise de sentimento usando TextBlob.
    Retorna uma tupla com a polaridade (positiva, negativa ou neutra)
    e a subjetividade do texto.
    '''
    blob = TextBlob(texto)
    polaridade = blob.sentiment.polarity
    subjetividade = blob.sentiment.subjectivity
    
    if polaridade > 0:
        sentimento = 'positivo'
    elif polaridade < 0:
        sentimento = 'negativo'
    else:
        sentimento = 'neutro'
    
    return sentimento, polaridade, subjetividade


def requestGetMusic(author, music):
    # Define o endpoint e os parâmetros da API
    api_url = 'https://api.vagalume.com.br/search.php'
    artist = author
    song = music

    # Crie a URL de solicitação com os parâmetros do artista e da música
    request_url = f'{api_url}?art={artist}&mus={song}'

    # Envia uma solicitação GET para a API
    response = requests.get(request_url)

    # Verifique se a solicitação foi bem-sucedida
    if response.status_code == 200:
        # Analisa a resposta JSON
        data = response.json()
        
        # Verifique se a letra foi encontrada
        if 'mus' in data and len(data['mus']) > 0:
            # Obtenha a letra da primeira música encontrada
            text = data['mus'][0]['text']
            # Print the lyrics
            #print(text)
            return text
        else:
            return print('Musica não encontrada.')
    else:
        return print('A requisição falhou.')


translator = Translator()
print('Escolha as opções: \n 1 - Analisar uma frase minha \n 2 - Analisar uma música ou trecho de música ')
optionAnalysis = input()


if optionAnalysis == '1':
    print('a opção escolhida foi analisar uma frase sua')
    text = input("Escreva o texto/frase para ser analisado: ")
    translated_text = translator.translate(text, src='pt', dest='en') #traduz o texto para inglês para ser analisado
    #print(translated_text.text)
else:
    print('Digite a musica e o auhtor que deseja analisar:')
    musica = input('Digite a musica: ')
    autor = input('Digite o autor: ')
    text = requestGetMusic(autor, musica)
    translated_text = translator.translate(text, src='pt', dest='en') #traduz a musica para inglês para ser analisado
    print(translated_text.text)

print('\n')
sentimento, polaridade, subjetividade = analisar_sentimento(translated_text.text)
print('Resultado da analise de sentimento: ')
print("Sentimento: ", sentimento)
print("Polaridade: ", polaridade)
print("Subjetividade: ", subjetividade)
