def ler_arquivo_gramatica(nome_arquivo):
    try:
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
                    parte_esquerda, parte_direita = linha.split(':', 1)  # separa apenas na primeira ocorrência de ':'
                    parte_esquerda = parte_esquerda.strip()
                    parte_direita = parte_direita.strip()

                    # Tratar o epsilon como cadeia vazia
                    if parte_direita == 'epsilon':
                        parte_direita = ''
                    
                    # Adicionar a produção
                    if parte_esquerda in gramatica['producoes']:
                        gramatica['producoes'][parte_esquerda].append(parte_direita)
                    else:
                        gramatica['producoes'][parte_esquerda] = [parte_direita]

            # Caso ainda não esteja nas produções, processar as variáveis, terminais e o símbolo inicial
            elif linha.startswith('variaveis:'):
                gramatica['variaveis'] = [v.strip() for v in linha.split(':')[1].split(',')]

            elif linha.startswith('inicial:'):
                gramatica['inicial'] = linha.split(':')[1].strip()

            elif linha.startswith('terminais:'):
                gramatica['terminais'] = [t.strip() for t in linha.split(':')[1].split(',')]

            elif linha.startswith('producoes'):
                producoes_comecaram = True  # Identificar que a seção de produções começou

        # Verifica se todas as seções têm pelo menos um valor
        if not gramatica['variaveis'] or not gramatica['inicial'] or not gramatica['terminais'] or not gramatica['producoes']:
            raise ValueError("Formato do arquivo errado: todas as seções devem conter pelo menos um valor.")

        return gramatica

    except FileNotFoundError:
        print(f"Erro: O arquivo '{nome_arquivo}' não foi encontrado.")
    except ValueError as e:
        print(e)
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")

    return None  # Retorna None em caso de erro
