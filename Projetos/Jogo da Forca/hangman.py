import random

word_list = ["camelo", "elefante", "barco", "sol"]
chosen_word = random.choice(word_list)

placeholder = ""
for position in range(len(chosen_word)):
    placeholder += "_"
print(placeholder)

game_over = False
correct_letters = []

while not game_over:
    guess = input('Adivinhe a palavra: ').lower()

    display = ""
    
    for letter in chosen_word:
            if letter == guess:
                display += letter
                correct_letters.append(guess)
            elif letter in correct_letters:
                display += letter
            else:
                display += "_"
    print(display)
    
    if "_" not in display:
        game_over = True
        print("Você venceu!")
