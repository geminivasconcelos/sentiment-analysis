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


translator = Translator()

text = input("Escreva o texto/frase para ser analisado: ")
translated_text = translator.translate(text, src='pt', dest='en')
print(translated_text.text)


sentimento, polaridade, subjetividade = analisar_sentimento(translated_text.text)
print("Sentimento: ", sentimento)
print("Polaridade: ", polaridade)
print("Subjetividade: ", subjetividade)


#observação: a analise de sentimento aqui está sendo feito em inglês, usei a biblioteca translate para pegar o texto digitado em português
# e traduzir para inglês e só então analisar a frase dita pelo usário e infomar o sentimento, subjetividade e polaridade;


