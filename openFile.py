import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# Baixar os recursos do NLTK necessários para a análise de sentimento
nltk.download('vader_lexicon')


#abre o arquivo, você passa o nome do arquivo e o objetivo dele
with open('email.txt', 'r') as arquivo:
    # Leia o conteúdo do arquivo
    avaliacoes = arquivo.read()
    # Faça o processamento necessário com o conteúdo do arquivo
    print(avaliacoes)


    # Inicializar o analisador de sentimento do NLTK
analisador_sentimento = SentimentIntensityAnalyzer()

# Realizar a análise de sentimento para cada avaliação
#for avaliacao in avaliacoes:
    # Remover quebras de linha e caracteres especiais
avaliacoes = avaliacoes.strip()
    
# Realizar a análise de sentimento
resultado = analisador_sentimento.polarity_scores(avaliacoes)
    
# Obter a pontuação de sentimento positivo, negativo e neutro
sentimento_positivo = resultado['pos']
sentimento_negativo = resultado['neg']
sentimento_neutro = resultado['neu']
    
    # Determinar o sentimento geral com base na pontuação
sentimento_geral = ''
if sentimento_positivo > sentimento_negativo:
    sentimento_geral = 'Positivo'
elif sentimento_negativo > sentimento_positivo:
     sentimento_geral = 'Negativo'
else:
    sentimento_geral = 'Neutro'
    
# Exibir o resultado da análise de sentimento
print('Avaliação: ', avaliacoes)
print('Sentimento geral: ', sentimento_geral)
print('Sentimento positivo: ', sentimento_positivo)
print('Sentimento negativo: ', sentimento_negativo)
print('Sentimento neutro: ', sentimento_neutro)
print('---')