def ler_arquivo_gramatica(nome_arquivo):
    with open(nome_arquivo, 'r') as arquivo:
        linhas = arquivo.readlines()

    gramatica = {
        'variaveis': [],
        'inicial': '',
        'terminais': [],
        'producoes': {}
    }

    producoes_comecaram = False  # Flag para identificar quando as produções começam

    for linha in linhas:
        linha = linha.strip()

        # Pular linhas vazias ou comentários
        if not linha or linha.startswith('#'):
            continue

        # Se estiver na seção de produções
        if producoes_comecaram:
            if ':' in linha:
                parte_esquerda, parte_direita = linha.split(':')
                parte_esquerda = parte_esquerda.strip()
                parte_direita = parte_direita.strip()

                # Tratar o epsilon como cadeia vazia
                if parte_direita == 'epsilon':
                    parte_direita = ' '
                
                # Adicionar a produção
                if parte_esquerda in gramatica['producoes']:
                    gramatica['producoes'][parte_esquerda].append(parte_direita)
                else:
                    gramatica['producoes'][parte_esquerda] = [parte_direita]

        # Caso ainda não esteja nas produções, processar as variáveis, terminais e o símbolo inicial
        elif linha.startswith('variaveis:'):
            gramatica['variaveis'] = linha.split(':')[1].split(',')

        elif linha.startswith('inicial:'):
            gramatica['inicial'] = linha.split(':')[1].strip()

        elif linha.startswith('terminais:'):
            gramatica['terminais'] = linha.split(':')[1].split(',')

        elif linha.startswith('producoes:'):
            producoes_comecaram = True  # Identificar que a seção de produções começou

    return gramatica
