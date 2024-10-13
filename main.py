from leitura import ler_arquivo_gramatica
from rapido import forma_cadeias

print('Bem-vindo ao Gerador de Cadeias para Gramáticas Livres de Contexto')

# Solicitar ao usuário o nome do arquivo da gramática
nome_arquivo = input("Digite o nome do arquivo da gramática (ex: gramatica.txt): ")
gramatica = ler_arquivo_gramatica(nome_arquivo)

# Exibir a gramática lida
print("Gramática lida:")
for chave, valor in gramatica.items():
    print(f"{chave}: {valor}")

# Solicitar ao usuário o número máximo de bits
tamanho = int(input("Digite o número máximo de bits para as cadeias: "))

# Gerar cadeias com o tamanho especificado
resultado = forma_cadeias(gramatica, tamanho=tamanho)

# Remover espaços das cadeias geradas
resultado = [item.replace(' ', '') for item in resultado]

# Exibir as cadeias formadas, cada uma em uma nova linha
print("Cadeias formadas:")
for cadeia in resultado:
    print(cadeia)
