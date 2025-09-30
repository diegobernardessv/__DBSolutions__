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

# --- Métodos essenciais para modificar listas ---
# append(item): Adiciona um item ao final da lista.
# insert(indice, item): Adiciona um item em uma posição específica.
# remove(item): Remove a primeira ocorrência de um item.
# pop(indice): Remove e retorna o item de um índice específico (se o índice não for informado, remove o último).
# sort(): Ordena a lista (modifica a lista original).

# Exemplo prático de manipulação.

tarefas_do_dia = ["Escovar os dentes ao acordar",
                  "Tomar café",
                  "Lavar o quintal",
                  "Fazer almoço",
                  "Dar comida ao cachorro"]

print(f"Tarefas iniciais: {tarefas_do_dia}")

# Adicionando novas tarefas
tarefas_do_dia.append("Estudar")
tarefas_do_dia.append("Lavar o carro")
tarefas_do_dia.append("Fazer o jantar")
tarefas_do_dia.append("Dormir")
tarefas_do_dia.insert(3, "Estudar Python")
print(f"Tarefas atualizadas: {tarefas_do_dia}")

# Removendo tarefas cumpridas
tarefas_do_dia.remove("Lavar o quintal")
tarefas_do_dia.remove("Fazer almoço")
tarefas_do_dia.remove("Dar comida ao cachorro")
print(f"Tarefas atualizadas: {tarefas_do_dia}")

# Removendo a última tarefa adicionada
tarefas_do_dia.pop()
print(f"Tarefas atualizadas: {tarefas_do_dia}")

# Ordenando a lista de tarefas em ordem crescente
tarefas_do_dia.sort()
print(f"Tarefas atualizadas: {tarefas_do_dia}")

# Ordenando a lista de tarefas em ordem decrescente
tarefas_do_dia.sort(reverse=True)
print(f"Tarefas atualizadas: {tarefas_do_dia}")

# --- Dicionários ---
# (Dicionários são coleções não ordenadas que armazenam dados no formato chave-valor.
# São extremamente eficientes para buscar informações.)

# Criando um dicionário para descrever um usuário.
usuario = {
    "nome": "Tobias Rieper",
    "idade": "28",
    "email": "tobiasrieper@gmail.com",
    "endereço": "Rua 47, Bielorússia",
    "telefone": "+55 27 983664533",
    "profissão": "Engenheiro de Software"
}

# Acessando valores através das chaves
print(f"Nome do usuário: {usuario['nome']}")
print(f"Idade do usuário: {usuario['idade']}")
print(f"Email do usuário: {usuario['email']}")

# Adicionando um novo par chave-valor
usuario["nacionalidade"] = "Italiano"
print(f"Nacionalidade do usuário adicionada: {usuario['nacionalidade']}")

# Modificando um valor existente
usuario["idade"] = 34
print(f"Idade do usuário modificada: {usuario['idade']}")
print(f"Dicionário atualizado: {usuario}")

# === Manipulando Dicionários com laços for
print("\n--- Chaves do Dicionário ---")


