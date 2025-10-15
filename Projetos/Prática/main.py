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
 /|\  | # type: ignore
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

# Lista de palavras expandida para aumentar a diversão!
lista_de_palavras = [
    "abrir", "adeus", "agora", "água", "ajudar", "aluno", "amarelo", "amar", "amanhã", "amigo", "amor",
    "aqui", "árvore", "atrás", "avó", "avô", "azul", "baixo", "banco", "beber", "bem", "branco", "bonito",
    "bom", "café", "cadeira", "cama", "carro", "casa", "cerveja", "certo", "chá", "claro", "começar",
    "comer", "comida", "como", "comprar", "criança", "cor", "coisa", "dar", "dentro", "desculpe", "dever",
    "dia", "difícil", "dinheiro", "dizer", "dormir", "enfermeiro", "então", "entre", "errado", "escola",
    "escrever", "escuro", "esperar", "estar", "estrela", "estudante", "fácil", "falar", "família",
    "fazer", "fechar", "feio", "feliz", "filho", "flor", "fora", "frente", "frio", "fruta", "gordo",
    "gostar", "grande", "homem", "hospital", "hoje", "idade", "ir", "irmã", "irmão", "janela", "laranja",
    "ler", "livro", "loja", "longe", "lua", "lugar", "magro", "mãe", "mão", "marrom", "mau", "médico",
    "menina", "menino", "mercado", "mesa", "morrer", "mulher", "mundo", "muito", "não", "nome", "novo",
    "nunca", "odiar", "olá", "olho", "ontem", "ouvir", "pai", "país", "pão", "pequeno", "perto", "pessoa",
    "pensar", "poder", "porta", "pouco", "preto", "prima", "primo", "professor", "quando", "querer",
    "rápido", "rato", "rinoceronte", "rosa", "roupa", "roxo", "rua", "saber", "sapato", "sempre",
    "sentir", "ser", "sim", "sobrenome", "sol", "sonhar", "talvez", "tempo", "terminar", "ter", "tia",
    "tio", "trabalho", "triste", "urso", "vender", "ver", "verde", "vermelho", "velho", "vinho", "vir",
    "viver", "você", "peru", "pica-pau", "pinguim", "pombo", "porco", "raposa", "sabiá", "sapo",
    "serpente", "siri", "sucuri", "suricate", "tartaruga", "tatu", "tigre", "toupeira", "touro",
    "tucano", "urubu", "vaca", "veado", "vespa", "zebra"
]


# Loop principal para permitir jogar novamente
while True:
    # --- Inicialização da Partida ---
    palavra_escolhida = random.choice(lista_de_palavras)
    vidas = VIDAS_INICIAIS
    game_over = False
    letras_tentadas = []

    # Cria o display inicial com underscores. Ex: ['_', '_', '_', '_']
    display = ["_" for _ in palavra_escolhida]
    print(f"{' '.join(display)}\n")

    # --- Loop da Partida ---
    while not game_over:
        chute = input("Adivinhe uma letra: ").lower()

        # Validação: Verifica se o jogador digitou apenas uma letra
        if not chute.isalpha() or len(chute) != 1:
            print("Por favor, digite apenas uma letra válida.")
            continue

        # Validação: Verifica se a letra já foi tentada
        if chute in letras_tentadas:
            print(f"Você já tentou a letra '{chute}'. Tente outra.")
            continue

        letras_tentadas.append(chute) # type: ignore

        # Verifica se o chute está na palavra
        if chute in palavra_escolhida:
            # Atualiza o display com a letra correta em todas as posições
            for i, letra in enumerate(palavra_escolhida):
                if letra == chute:
                    display[i] = chute
            print(f"\nBoa! A letra '{chute}' está na palavra.")
        else:
            # Condição de perda de vida
            vidas -= 1
            print(f"\nVocê errou! A letra '{chute}' não está na palavra. Vidas restantes: {vidas}")
            print(stages[vidas])

        # Mostra o estado atual do display
        print(f"{' '.join(display)}")

        # Condição de vitória
        if "_" not in display:
            game_over = True
            print("\n🎉 Parabéns, você ganhou! 🎉")

        # Condição de derrota
        if vidas == 0:
            game_over = True
            print("\n☠️ Game Over! Você ficou sem vidas. ☠️")
            print(f"A palavra era: {palavra_escolhida.capitalize()}")

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
