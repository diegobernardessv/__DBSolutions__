import random

print("=== Bem vindo ao jogo da Forca! ===")

stages = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

# Invertendo a lista para que o número de vidas corresponda ao índice
stages.reverse()

VIDAS_INICIAIS = 6

word_list = ["ilha", "amsterdam", "alemanha", "roma"]

while True:
    chosen_word = random.choice(word_list)
    vidas = VIDAS_INICIAIS
    game_over = False
    correct_letters = []

    placeholder = ""
    for _ in range(len(chosen_word)):
        placeholder += "_"
    print(placeholder)

    while not game_over:
        guess = input("Guess a letter: ").lower()

        display = ""

        for letter in chosen_word:
            if letter == guess:
                display += letter
                correct_letters.append(letter)
            elif letter in correct_letters:
                display += letter
            else:
                display += "_"
        print(display)

        # Condição de vitória
        if "_" not in display:
            game_over = True
            print("\n🎉 Parabéns, você ganhou! 🎉")

        # Condição de perda de vida
        if guess not in chosen_word:
            vidas -= 1
            print(f"Você errou! A letra '{guess}' não está na palavra. Vidas restantes: {vidas}")
            print(stages[vidas])

        # Condição de derrota
        if vidas == 0:
            game_over = True
            print("\n☠️ Game Over! Você ficou sem vidas. ☠️")
            print(f"A palavra era: {chosen_word.capitalize()}")  # Mostra a palavra correta

    # --- Fim da Partida ---
    # Pergunta ao jogador se ele quer jogar novamente
    while True:
        jogar_novamente = input("\nDeseja jogar novamente? (s/n): ").lower()
        if jogar_novamente in ["s", "sim"]:
            break  # Sai deste loop interno para começar uma nova partida
        elif jogar_novamente in ["n", "nao", "não"]:
            print("Obrigado por jogar! Até a próxima.")
            exit()  # Encerra o programa
        else:
            print("Opção inválida. Por favor, digite 's' para sim ou 'n' para não.")
