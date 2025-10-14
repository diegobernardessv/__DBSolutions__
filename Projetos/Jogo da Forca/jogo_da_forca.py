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

# Lista de palavras
lista_de_palavras = [
    "abrir", "adeus", "agora", "água", "ajudar", "aluno", "amarelo", "amar", "amanhã", "amigo", "amor",
    "aqui", "árvore", "atrás", "avó", "avô", "azul", "baixo", "banco", "beber", "bem", "branco", "bonito",
    "bom", "bom dia", "boa tarde", "boa noite", "café", "cadeira", "cama", "carro", "casa", "cerveja",
    "certo", "chá", "claro", "começar", "comer", "comida", "como", "comprar", "criança", "cor", "coisa",
    "dar", "dentro", "desculpe", "dever", "dia", "difícil", "dinheiro", "dizer", "dormir", "enfermeiro",
    "então", "entre", "errado", "escola", "escrever", "escuro", "esperar", "estar", "estrela", "estudante",
    "fácil", "falar", "família", "fazer", "fechar", "feio", "feliz", "filho", "flor", "fora", "frente",
    "frio", "fruta", "gordo", "gostar", "grande", "homem", "hospital", "hoje", "idade", "ir", "irmã",
    "irmão", "janela", "laranja", "ler", "livro", "loja", "longe", "lua", "lugar", "magro", "mãe", "mão",
    "marrom", "mau", "médico", "menina", "menino", "mercado", "mesa", "morrer", "mulher", "mundo", "muito",
    "não", "nome", "novo", "nunca", "odiar", "olá", "olho", "ontem", "ouvir", "pai", "país", "pão", "pequeno",
    "perto", "pessoa", "pensar", "poder", "por favor", "porta", "pouco", "preto", "prima", "primo",
    "professor", "quando", "querer", "rápido", "rato", "rinoceronte", "rosa", "roupa", "roxo", "rua",
    "saber", "sapato", "sempre", "sentir", "ser", "sim", "sobrenome", "sol", "sonhar", "talvez", "tempo",
    "terminar", "ter", "tia", "tio", "trabalho", "triste", "urso", "vender", "ver", "verde", "vermelho",
    "velho", "vinho", "vir", "viver", "você",
    # Animais
    "Peru", "Pica-pau", "Pinguim", "Pombo", "Porco", "Porco-espinho", "Raposa", "Sabiá", "Sapo", "Serpente",
    "Siri", "Sucuri", "Suricate", "Tartaruga", "Tatu", "Tigre", "Toupeira", "Touro", "Tucano", "Urubu",
    "Vaca", "Vaga-lume", "Veado", "Vespa", "Zebra"
]

VIDAS_INICIAIS = 6

# Loop principal para permitir jogar novamente
while True:
    # --- Inicialização da Partida ---
    palavra_aleatoria = random.choice(lista_de_palavras).lower()
    display_atual = ["_" for _ in range(len(palavra_aleatoria))]
    vidas = VIDAS_INICIAIS
    game_over = False
    letras_tentadas = []

    print(" ".join(display_atual))
    print(stages[vidas])
    # --- Fim da Inicialização da Partida ---

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
            continue
        
        letras_tentadas.append(chute) # Adiciona a letra à lista de letras tentadas

        acertou_na_rodada = False # Flag para verificar se o chute foi correto nesta rodada
        
        # Verifica se a letra está na palavra aleatória e atualiza o display_atual
        for i, letra_da_palavra in enumerate(palavra_aleatoria):
            if letra_da_palavra == chute:
                display_atual[i] = chute # Atualiza a posição no display_atual
                acertou_na_rodada = True

        # Imprime a mensagem de erro apenas uma vez se o chute foi incorreto
        if not acertou_na_rodada:
            vidas -= 1 # Decrementa vidas se errou
            print(f"Você errou! A letra '{chute}' não está na palavra. Vidas restantes: {vidas}")
            print(stages[vidas]) # Mostra o estágio atual da forca
        else:
            print(f"Boa! A letra '{chute}' está na palavra.")

        print(" ".join(display_atual)) # Imprime o estado atualizado da palavra

        # Condição de vitória
        if "_" not in display_atual:
            game_over = True
            print("\n🎉 Parabéns, você ganhou! 🎉")
        
        # Condição de derrota
        if vidas == 0:
            game_over = True
            print("\n☠️ Game Over! Você ficou sem vidas. ☠️")
            print(f"A palavra era: {palavra_aleatoria.capitalize()}") # Mostra a palavra correta

    # --- Fim da Partida ---
    # Pergunta ao jogador se ele quer jogar novamente
    while True:
        jogar_novamente = input("\nDeseja jogar novamente? (s/n): ").lower()
        if jogar_novamente in ["s", "sim"]:
            break # Sai deste loop interno para começar uma nova partida
        elif jogar_novamente in ["n", "nao", "não"]:
            print("Obrigado por jogar! Até a próxima.")
            exit() # Encerra o programa
        else:
            print("Opção inválida. Por favor, digite 's' para sim ou 'n' para não.")

        
