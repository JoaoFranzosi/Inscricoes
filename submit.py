import cgi

MAX_INSCRICOES = 25

form = cgi.FieldStorage()
nome = form.getvalue('nome')
celular = form.getvalue('celular')

# Abre o arquivo de inscrições
with open('inscricoes.txt', 'a') as f:
    # Verifica se ainda há vagas disponíveis
    if len(f.readlines()) < MAX_INSCRICOES:
        # Escreve a nova inscrição no arquivo
        f.write(f'{nome};{celular}\n')
        print('Content-type: text/html')
        print()
        print('<h1>Inscrição realizada com sucesso!</h1>')
    else:
        print('Content-type: text/html')
        print()
        print('<h1>As inscrições já foram encerradas.</h1>')
