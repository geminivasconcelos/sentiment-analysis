
#abre o arquivo, você passa o nome do arquivo e o objetivo dele
with open('email.txt', 'r') as arquivo:
    # Leia o conteúdo do arquivo
    conteudo = arquivo.read()
    # Faça o processamento necessário com o conteúdo do arquivo
    print(conteudo)