def forma_cadeias_detalhado(glc):
    # Extrai as variáveis, símbolos terminais, variável inicial e produções da gramática
    variaveis = glc['variaveis']
    simbolos = glc['terminais']
    variavel_de_partida = glc['inicial']
    producoes = glc['producoes']

    # Inicializa a cadeia atual com a variável inicial
    cadeia_atual = variavel_de_partida
    while True:
        # Exibe a cadeia atual
        print(f"Cadeia atual: {cadeia_atual}")
        print("Producoes disponiveis:")

        # Lista para armazenar as produções possíveis
        producoes_possiveis = []
        for i, char in enumerate(cadeia_atual):
            # Verifica se o caractere atual é uma variável
            if char in variaveis:
                # Adiciona todas as produções possíveis para a variável
                for prod in producoes[char]:
                    producoes_possiveis.append((i, char, prod))

        # Se não houver produções possíveis, encerra o loop
        if not producoes_possiveis:
            print("Nenhuma produção disponível. Cadeia final: ", cadeia_atual)
            break

        # Exibe as produções possíveis para o usuário escolher
        for idx, (pos, var, prod) in enumerate(producoes_possiveis):
            print(f"{idx + 1}: substituir {var} por {prod} na posição {pos}")

        # Solicita ao usuário que escolha uma produção
        escolha = int(input("Escolha a produção (digite o número): ")) - 1
        pos, var, prod = producoes_possiveis[escolha]

        # Atualiza a cadeia atual com a produção escolhida
        cadeia_atual = cadeia_atual[:pos] + cadeia_atual[pos:].replace(var, prod, 1)


    # Retorna a cadeia final
    return cadeia_atual

