
print(''' _                                                           
| |                                                          
| |_ _ __ ___  __ _ ___ _   _ _ __ ___ _ __ ___   __ _ _ __  
| __| '__/ _ \/ _` / __| | | | '__/ _ \ '_ ` _ \ / _` | '_ \ 
| |_| | |  __/ (_| \__ \ |_| | | |  __/ | | | | | (_| | |_) |
 \__|_|  \___|\__,_|___/\__,_|_|  \___|_| |_| |_|\__,_| .__/ 
                                                      | |    
                                                      |_|    ''')
print('''  ____________________________________________________________________
 / \-----     ---------  -----------     -------------- ------    ----\
 \_/__________________________________________________________________/
 |~ ~~ ~~~ ~ ~ ~~~ ~ _____.----------._ ~~~  ~~~~ ~~   ~~  ~~~~~ ~~~~|
 |  _   ~~ ~~ __,---'_       "         `. ~~~ _,--.  ~~~~ __,---.  ~~|
 | | \___ ~~ /      ( )   "          "   `-.,' (') \~~ ~ (  / _\ \~~ |
 |  \    \__/_   __(( _)_      (    "   "     (_\_) \___~ `-.___,'  ~|
 |~~ \     (  )_(__)_|( ))  "   ))          "   |    "  \ ~~ ~~~ _ ~~|
 |  ~ \__ (( _( (  ))  ) _)    ((     \\//    " |   "    \_____,' | ~|
 |~~ ~   \  ( ))(_)(_)_)|  "    ))    //\\ " __,---._  "  "   "  /~~~|
 |    ~~~ |(_ _)| | |   |   "  (   "      ,-'~~~ ~~~ `-.   ___  /~ ~ |
 | ~~     |  |  |   |   _,--- ,--. _  "  (~~  ~~~~  ~~~ ) /___\ \~~ ~|
 |  ~ ~~ /   |      _,----._,'`--'\.`-._  `._~~_~__~_,-'  |H__|  \ ~~|
 |~~    / "     _,-' / `\ ,' / _'  \`.---.._          __        " \~ |
 | ~~~ / /   .-' , / ' _,'_  -  _ '- _`._ `.`-._    _/- `--.   " " \~|
 |  ~ / / _-- `---,~.-' __   --  _,---.  `-._   _,-'- / ` \ \_   " |~|
 | ~ | | -- _    /~/  `-_- _  _,' '  \ \_`-._,-'  / --   \  - \_   / |
 |~~ | \ -      /~~| "     ,-'_ /-  `_ ._`._`-...._____...._,--'  /~~|
 | ~~\  \_ /   /~~/    ___  `---  ---  - - ' ,--.     ___        |~ ~|
 |~   \      ,'~~|  " (o o)   "         " " |~~~ \_,-' ~ `.     ,'~~ |
 | ~~ ~|__,-'~~~~~\    \"/      "  "   "    /~ ~~   O ~ ~~`-.__/~ ~~~|
 |~~~ ~~~  ~~~~~~~~`.______________________/ ~~~    |   ~~~ ~~ ~ ~~~~|
 |____~jrei~__~_______~~_~____~~_____~~___~_~~___~\_|_/ ~_____~___~__|
 / \----- ----- ------------  ------- ----- -------  --------  -------\
 \_/__________________________________________________________________/''')
print("Bem vindo á ilha do tesouro Python!")
print("Sua missão é encontrar o tesouro.")

choice1 = input('Você chega em uma ilha, e se depara com uma encruzilhada. Qual direção você quer seguir?\nDigite "esquerda" ou "direita": ').lower()

if choice1 == "esquerda":
    # Continu
    choice2 = input('Você encontra um oasis, com águas revigorantes, e decide descansar um pouco.'
                    'Você se levanta, e começa a caminhar. Chega em frente a um grande lago.'
                    'Tem uma ilha no meio do lago.\n'
                    'Digite "nadar" para tentar chegar até a ilha nadando, ou "esperar" para esperar um barco: ').lower()
    if choice2 == "esperar":
        choice3 = input('Você chegou na ilha à salvo.'
                        'Você se depara com uma casa com 3 portas de cores diferentes, e um aviso dizendo que o tesouro está dentro de apenas 1 delas, e você têm apenas 1 chance para escolher.'
                        'Uma porta é amarela, com o símbolo do sol.\n'
                        'Uma porta é azul, com o símbolo de um buraco negro.\n'
                        'E uma porta é vermelha, com traços de sangue.\n'
                        'Qual porta você escolhe? ').lower()
        if choice3 == "vermelha":
            print('A sala está cheia de adagas, que voam na sua direção. Game over.')
        elif choice3 == "azul":
            print('Ao se adentrar na sala, você cai em um buraco negro. Game over.')
        elif choice3 == "amarela": 
            print('Parabéns! Você encontrou o tesouro, que está cheio de moedas e barras de ouro!')
        else:
            # Game Over
            print('Opção errada.')
    
    else:
        # Game Over
        print('A maré está muito cheia, e você cai em um buraco dentro da água. It\'s over pra você.')
else:
    # Game Over
    print('Você dá de cara com um Tiranossauro Rex. Você tenta de esquivar dele, mas ele é mais rápido do que você. Game over.')

        
        
