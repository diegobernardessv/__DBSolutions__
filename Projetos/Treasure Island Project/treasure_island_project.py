import time

def introducao():
    """Exibe a introdução do jogo."""
    print(r''' _                                     _     _                 _
| |                                   (_)   | |               | |
| |_ _ __ ___  __ _ ___ _   _ _ __ ___ _ ___| | __ _ _ __   __| |
| __| '__/ _ \/ _` / __| | | | '__/ _ \ / __| |/ _` | '_ \ / _` |
| |_| | |  __/ (_| \__ \ |_| | | |  __/ \__ \ | (_| | | | | (_| |
 \__|_|  \___|\__,_|___/\__,_|_|  \___|_|___/_|\__,_|_| |_|\__,_|''')
    print("\n" + "="*35)
    print("=== Bem-vindo à Ilha do Tesouro ===")
    print("=== Sua missão é encontrar o ouro ===")
    print("="*35 + "\n")
    time.sleep(2)
    print("Você acorda em uma praia desconhecida, com a memória turva...")
    time.sleep(2)
    print("À sua frente, a selva densa se ergue, e um caminho se divide em dois.")
    time.sleep(1)

def game_over(mensagem: str):
    """Função para finalizar o jogo em caso de derrota."""
    print("\n" + mensagem)
    print("☠️  GAME OVER ☠️")

def vitoria():
    """Função para finalizar o jogo em caso de vitória."""
    print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"--._o_._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/____/______/______/______/
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
    print("\nParabéns! Você superou os perigos da ilha e encontrou o tesouro perdido!")
    print("✨ VOCÊ VENCEU! ✨")

def escolher_porta():
    """Terceira etapa: as três portas."""
    time.sleep(1)
    print("\nApós uma curta viagem, o barco chega à ilha central.")
    time.sleep(2)
    print("Você encontra as ruínas de um templo antigo. Na entrada, três portas se apresentam:")
    print("Uma porta VERMELHA, coberta de runas que parecem pulsar com calor.")
    print("Uma porta AZUL, de onde emana um frio sobrenatural e um silêncio profundo.")
    print("Uma porta AMARELA, que brilha com uma luz quente e convidativa.")
    time.sleep(1)
    
    escolha = input("\nQual porta você escolhe? (vermelha/azul/amarela): ").lower()

    if escolha == "amarela":
        vitoria()
    elif escolha == "vermelha":
        game_over("Ao tocar na porta vermelha, ela explode em chamas. Você foi consumido pelo fogo.")
    elif escolha == "azul":
        game_over("A porta azul se abre para um vácuo escuro. Você é sugado para o nada.")
    else:
        game_over("Hesitante, você não escolhe nenhuma porta. O chão sob seus pés desmorona e você cai na escuridão.")

def beira_do_lago():
    """Segunda etapa: o lago."""
    time.sleep(1)
    print("\nO caminho da esquerda te leva à beira de um grande lago de águas escuras.")
    time.sleep(2)
    print("No meio do lago, você avista uma pequena ilha com o que parece ser um templo.")
    time.sleep(1)
    print("A água parece perigosa, mas você vê um pequeno barco a remo amarrado a uma árvore.")

    escolha = input("\nVocê tenta NADAR através do lago ou usa o BARCO para atravessar? (nadar/barco): ").lower()

    if escolha == "barco":
        escolher_porta()
    elif escolha == "nadar":
        game_over("Assim que você entra na água, criaturas sombrias te puxam para o fundo. A última coisa que você vê são olhos brilhantes na escuridão.")
    else:
        game_over("Enquanto você decidia, uma criatura gigante emergiu do lago e te devorou.")

def iniciar_jogo():
    """Função que inicia e controla o fluxo do jogo."""
    introducao()
    escolha = input("Qual caminho você quer seguir? (esquerda/direita): ").lower()

    if escolha == "esquerda":
        beira_do_lago()
    elif escolha == "direita":
        game_over("O caminho da direita leva a um penhasco escondido. Você não vê a tempo e cai para a morte.")
    else:
        game_over("Você não conseguiu se decidir e uma onça pintada te encontrou. Foi um final rápido.")

# --- Loop Principal do Jogo ---
while True:
    iniciar_jogo()
    
    jogar_novamente = input("\nDeseja jogar novamente? (s/n): ").lower()
    if jogar_novamente not in ["s", "sim"]:
        print("\nObrigado por se aventurar na Ilha do Tesouro!")
        break
