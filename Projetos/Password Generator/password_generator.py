import random

letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]

print('''  ad8888888888ba
 dP'         `"8b,
 8  ,aaa,       "Y888a     ,aaaa,     ,aaa,  ,aa,
 8  8' `8           "88baadP""""YbaaadP"""YbdP""Yb
 8  8   8              """        """      ""    8b
 8  8, ,8         ,aaaaaaaaaaaaaaaaaaaaaaaaddddd88P
 8  `"""'       ,d8""
 Yb,         ,ad8"
  "Y8888888888P"''')
print(" ")
print("Bem vindo ao Gerador PyPasswords!")
print(" ")

nr_letters = int(input("Quantas letras gostaria de ter na sua senha?\n"))
nr_symbols = int(input("Quantos símbolos gostaria de ter na sua senha?\n"))
nr_numbers = int(input("Quantos números gostaria de ter na sua senha?\n"))

# Criando uma nova lista com a quantidade de caracteres escolhida
password_list = []

for char in range(0, nr_letters):
    password_list.append(random.choice(letters))

for char in range(0, nr_symbols):
    password_list.append(random.choice(symbols))
  
for char in range(0, nr_numbers):
    password_list.append(random.choice(numbers))

# Randomizando o password para ficar inquebrável
random.shuffle(password_list)

# Apresentando a senha criada ao usuário
password = ""
for char in password_list:
    password += str(char)

print(f"Sua nova senha é: {password}")
    
