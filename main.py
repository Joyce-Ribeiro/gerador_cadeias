from leitura import ler_arquivo_gramatica
from rapido import forma_cadeias
print('Bem vindo ao Gerador de cadeias para Gramaticas Livres de Contexto')
nome_arquivo = 'gramatica.txt'
gramatica = ler_arquivo_gramatica(nome_arquivo)

print(gramatica)
resultado = forma_cadeias(gramatica, tamanho=3)
resultado = [item.replace(' ', '') for item in resultado]
print("cadeias formadas:", resultado)