def conta_simbolos(cadeia, simbolos):
    # Conta quantos símbolos terminais existem na cadeia
    return sum(1 for char in cadeia if char in simbolos)

def nao_contem_variavel(cadeia, variaveis):
    # Verifica se a cadeia contém alguma variável
    return all(char not in variaveis for char in cadeia)

def forma_cadeias(glc, tamanho, cadeias_formadas):
    variaveis = glc['variaveis']
    simbolos = glc['terminais']
    variavel_de_partida = glc['inicial']
    producoes = glc['producoes']

    fila_producoes = [] # Producoes que faltam
    cadeias_formadas_totais = []# Todas as cadeias_formadas geradas ate o momento (com ou sem simbolos)

    # Adiciona as producoes que partem da variável de partida
    for p in producoes.get(variavel_de_partida, []):
        fila_producoes.append(p)
        cadeias_formadas_totais.append(p)

    while fila_producoes: # Enquanto existir producoes:
        p_aux = fila_producoes.pop(0) # Seleciona a primeira produção

        for variavel in variaveis: # Seleciona a Primeira variavel
            for p in producoes.get(variavel, []):
                # Substitui a primeira ocorrência onde a variavel p pode ser substituída
                cadeia = p_aux.replace(variavel, p, 1)

                if conta_simbolos(cadeia, simbolos) <= tamanho: # Se ao substituir *não* passar do tamanho estabelecido
                    if nao_contem_variavel(cadeia, variaveis) and cadeia not in cadeias_formadas: # Se não existe mais variaveis na cadeia
                        cadeias_formadas.append(cadeia)

                    elif cadeia not in cadeias_formadas_totais and cadeia not in cadeias_formadas:  # Se a cadeia nunca foi adicionada na lista e contém variável
                        fila_producoes.append(cadeia) 
                        cadeias_formadas_totais.append(cadeia)

                    if conta_simbolos(cadeia, simbolos) > tamanho: # Se a quantidade de simbolos passar do tamanho estabelecido (não for possivel criar uma cadeia minima)
                        print("Quantidade de símbolos maior que o tamanho:", conta_simbolos(cadeia, simbolos))

    return cadeias_formadas, cadeias_formadas_totais
