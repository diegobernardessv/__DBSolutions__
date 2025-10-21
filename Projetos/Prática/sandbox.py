import random

letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numeros = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
simbolos = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

nr_letras = int(input("Quantas letras gostaria de ter na sua senha? \n"))
nr_numeros = int(input("Quantos números gostaria de ter na sua senha? \n"))
nr_simbolos = int(input("Quantos símbolos gostaria de ter na sua senha? \n"))

lista_senha = []

for char in range(0, nr_letras):
    lista_senha.append(random.choice(letras))
    
for char in range(0, nr_numeros):
    lista_senha.append(random.choice(numeros))
    
for char in range(0, nr_simbolos):
    lista_senha.append(random.choice(simbolos))
    
random.shuffle(lista_senha)

senha_aleatoria = ""
for char in lista_senha:
    senha_aleatoria += char
    
print(f"Sua nova senha é: {senha_aleatoria}")