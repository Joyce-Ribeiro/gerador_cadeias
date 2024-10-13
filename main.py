from leitura import ler_arquivo_gramatica
from rapido import forma_cadeias

print('Bem-vindo ao Gerador de Cadeias para Gramáticas Livres de Contexto')

# Solicitar ao usuário o nome do arquivo da gramática
nome_arquivo = input("Digite o nome do arquivo da gramática (ex: gramatica.txt): ")
gramatica = ler_arquivo_gramatica(nome_arquivo)
res = []

# Exibir a gramática lida
if gramatica:
    print("Gramática lida:")
    for chave, valor in gramatica.items():
        print(f"{chave}: {valor}")

    while True:
        # Solicitar ao usuário o número máximo de bits
        tamanho = int(input("Digite o número máximo de bits para as cadeias: "))
        cadeias_formadas = []  # Cadeias formadas finais

        # Gerar cadeias com o tamanho especificado
        resultado, producoes = forma_cadeias(gramatica, tamanho=tamanho, cadeias_formadas=cadeias_formadas)

        # Exibir as cadeias formadas com suas produções
        print("Cadeias formadas com suas produções:")
        for cadeia, p in zip(resultado, producoes):
            # Verificar se a cadeia e produção já foram registradas
            if [cadeia, p] not in res:
                print(cadeia, "->", p)
                res.append([cadeia, p])

        # Perguntar ao usuário se deseja gerar uma nova cadeia
        continuar = input("Deseja gerar uma nova cadeia? (s/n): ").strip().lower()
        if continuar != 's':
            break

    print("Obrigado por usar o Gerador de Cadeias!")
