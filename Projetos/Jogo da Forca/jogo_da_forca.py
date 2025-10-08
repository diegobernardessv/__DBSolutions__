import random

print("=== Bem vindo ao jogo da forca ===")

# Escolhe uma palavra aleatória da lista de palavras
lista_de_palavras = ["Camelo", "Elefante", "Barco", "Sol", "Mumia", "Francesa", "Deus", "Esfinge"]
palavra_aleatoria = random.choice(lista_de_palavras).lower() # Converte a palavra para minúsculas 

# Lista para facilitar a atualização de letras em posições específicas.
display_atual = ["_" for _ in range(len(palavra_aleatoria))]
print(" ".join(display_atual)) # Imprime o estado inicial da palavra com espaços para melhor leitura

game_over = False
letras_adivinhadas_corretamente = [] # Armazena as letras que o jogador adivinhou corretamente
letras_tentadas = [] # Armazena todas as letras que o jogador já tentou (para evitar repetições)
vidas = 6 # Contador de vidas

while not game_over:
    # Pede ao jogador para adivinhar uma letra    
    chute = input("Digite uma letra: ").lower()
    
    # Validação básica do input
    if not chute.isalpha() or len(chute) != 1:
        print("Por favor, digite apenas uma letra válida.")
        continue
    
    # Verifica se a letra já foi tentada
    if chute in letras_tentadas:
        print(f"Você já tentou a letra '{chute}'. Tente outra.")
        print(" ".join(display_atual)) # Mostra o display atual novamente
        continue
    
    letras_tentadas.append(chute) # Adiciona a letra à lista de letras tentadas

    acertou_na_rodada = False # Flag para verificar se o chute foi correto nesta rodada
    
    # Verifica se a letra está na palavra aleatória e atualiza o display_atual
    for i, letra_da_palavra in enumerate(palavra_aleatoria):
        if letra_da_palavra == chute:
            display_atual[i] = chute # Atualiza a posição no display_atual
            acertou_na_rodada = True
            if chute not in letras_adivinhadas_corretamente: # Adiciona a letra à lista de corretas apenas uma vez
                letras_adivinhadas_corretamente.append(chute)

    # Imprime a mensagem de erro apenas uma vez se o chute foi incorreto
    if not acertou_na_rodada:
        vidas -= 1 # Decrementa vidas se errou
        print(f"Você errou! A letra '{chute}' não está na palavra. Vidas restantes: {vidas}")
    else:
        print(f"Boa! A letra '{chute}' está na palavra.")

    print(" ".join(display_atual)) # Imprime o estado atualizado da palavra

    # Condição de vitória
    if "_" not in display_atual:
        game_over = True
        print("Você ganhou!")
    
    # Condição de derrota
    if vidas == 0:
        game_over = True
        print("Game Over! Você ficou sem vidas.")
        print(f"A palavra era: {palavra_aleatoria.capitalize()}") # Mostra a palavra correta
        
