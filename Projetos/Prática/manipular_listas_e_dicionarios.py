# Listas (A verdadeira força das listas aparece quando você as percorre para ler ou modificar seus dados.)
# Criando uma lista de frutas
frutas = ["maçã", "banana", "melancia", "pera", "kiwi", "morango", "abacate", "manga", "laranja", "abacaxi", "uva", "melão"]

# Criando uma lista de números inteiros
numeros = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

# Acessando os elementos pelo índice
primeira_fruta = frutas[0]
segundo_numero = numeros[1]
print(f"A quarta fruta da lista é {frutas[3]}.")
print(f"A primeira fruta é {primeira_fruta}.")
print(f"O segundo número é {segundo_numero}.")

# Acessando os elementos pelo índice negativo
ultima_fruta = frutas[-1]
penultimo_numero = numeros[-2]
print(f"A última fruta é {ultima_fruta}.")
print(f"O penúltimo número é {penultimo_numero}.")

# Iterando sobre as listas com for loop
for numero in numeros:
    print(f"Número sorteado: {numero}")

for fruta in frutas:
    print(f"Eu gosto de {fruta}.")

# Dobrar cada número em uma nova lista
numeros_dobrados = []

for numero in numeros:
    dobro = numero * 2
    numeros_dobrados.append(dobro)

print(f"Números originais: {numeros}")
print(f"Números dobrados: {numeros_dobrados}")

# Descontar 10% de cada número da nova lista
numeros_descontados = []

for numero in numeros_dobrados:
    desconto = numero * 0.9
    numeros_descontados.append(desconto)

print(f"Números com 10% de desconto incluído: {numeros_descontados}")

# While loop (O while é útil quando você precisa controlar o índice manualmente ou a condição de parada é mais complexa.)
print("--- Frutas até encontrar laranja (com while) ---")

i = 0 # Variável de controle (índice)
while i < len(frutas): # len() retorna o tamanho da lista
    fruta_atual = frutas[i]
    if fruta_atual == "laranja":
        print("Encontrei a laranja! Parando.")
        break # O comando 'break' para o laço
    print(f"Ainda não é a laranja. Esta é a fruta atual: {fruta_atual}.")
    i += 1 # Importante: incrementar o contador para não criar um loop infinito



