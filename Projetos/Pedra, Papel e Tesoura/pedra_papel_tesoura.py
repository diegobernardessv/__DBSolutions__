import random

print('Bem vindo ao Pedra, Papel e Tesoura Oficial Game !')

# Rock
pedra = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)

# Pedra
"""

# Paper
papel = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)

# Papel
"""

# Scissors
tesoura = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)

# Tesoura
"""

game_images = [pedra, papel, tesoura]

user_choice = int(input('O que você escolhe? Digite 0 para Pedra, 1 para Papel ou 2 para Tesoura: '))

if user_choice >= 0 and user_choice <= 2:
    print(f"Você escolheu: \n{game_images[user_choice]}")
    
computer_choice = random.randint(0,2)
print(f'Computador escolheu: \n{game_images[computer_choice]}')

if user_choice == 0 and computer_choice == 2:
    print('Você ganhou !')
elif computer_choice == 0 and user_choice == 2:
    print('Você perdeu !')
elif computer_choice > user_choice:
    print('Você perdeu !')
elif user_choice > computer_choice:
    print('Você ganhou !')
elif computer_choice == user_choice:
    print('Empate !')
else:
    print('Você digitou um número inválido, você perdeu !')