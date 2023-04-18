from textblob import TextBlob
import nltk

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

# Exemplo de uso
texto = "Eu odeio essa nova música! É horrível!"
sentimento, polaridade, subjetividade = analisar_sentimento(texto)
print("Sentimento: ", sentimento)
print("Polaridade: ", polaridade)
print("Subjetividade: ", subjetividade)
