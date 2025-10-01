import string # Para ajudar a remover pontuação

texto_modelo = """
Python é uma linguagem de programação de alto nível, interpretada, de script,
imperativa, orientada a objetos, funcional, de tipagem dinâmica e forte.
Foi lançada por Guido van Rossum em 1991. Atualmente, possui um modelo de
desenvolvimento comunitário, aberto e gerenciado pela organização sem fins
lucrativos Python Software Foundation. A linguagem foi projetada com a
filosofia de enfatizar a importância do esforço do programador sobre o
esforço computacional. Favorece a legibilidade do código sobre a velocidade
ou expressividade. Python é uma linguagem que suporta múltiplos paradigmas
de programação.
"""

# 1. Preparar o texto: minúsculas e sem pontuação
texto_limpo = texto_modelo.lower()

# A linha abaixo substitui cada pontuação por um espaço em branco
for pontuacao in string.punctuation:
    texto_limpo = texto_limpo.replace(pontuacao, " ")

# 2. Dividir o texto em uma lista de palavras
palavras = texto_limpo.split()

# 3. Contar a frequência de cada palavra usando um dicionário
frequencia_palavras = {}
for palavra in palavras:
    if palavra in frequencia_palavras:
        frequencia_palavras[palavra] += 1
    else:
        frequencia_palavras[palavra] = 1

# 4. Converter o dicionário em uma lista de tuplas para ordenar
# .items() cria uma lista de pares (chave, valor), ex: [('python', 3), ('é', 2)]
lista_frequencia = list(frequencia_palavras.items())

# 5. Ordenar a lista pela frequência (o segundo item da tupla, índice 1)
# O argumento 'key' diz para a função de ordenação olhar para o segundo elemento (x[1])
# 'reverse=True' ordena do maior para o menor
lista_frequencia.sort(key=lambda item: item[1], reverse=True)

# 6. Exibir os resultados
print("=== Análise de Frequência de Palavras")
print(f"Total de palavras únicas: {len(frequencia_palavras)}")
print("\nAs 5 palavras mais comuns são:")
for i in range(5):
    palavra, contagem = lista_frequencia[i]
    print(f"{i+1}. '{palavra}' - aparece {contagem} vezes")
