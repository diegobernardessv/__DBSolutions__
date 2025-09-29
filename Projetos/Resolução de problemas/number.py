def max_of_two_number():
    num1 = int(input("Digite um número: "))
    num2 = int(input("Digite outro número: "))

    largest = max(num1, num2)
    print(f"O maior número é: {largest}")
    
def max_of_five_numbers():
    num1 = int(input("Digite um número: "))
    num2 = int(input("Digite outro número: "))
    num3 = int(input("Digite outro número: "))
    num4 = int(input("Digite outro número: "))
    num5 = int(input("Digite outro número: "))

    largest = max(num1, num2, num3, num4, num5)
    print(f"O maior número é: {largest}")
    
def media_numeros():
    len = int(input("Quantos números você quer digitar? "))
    
    numeros = []
    
    for i in range(0, len):
        num = int(input("Digite um número: "))
        numeros.append(num)
    
    total = sum(numeros)
    media = total / len
    
    print(f"A média dos números é: {media}")

def divisivel_por_3_e_5():
    len = int(input("Quantos números você quer verificar? "))
    
    numeros = []
    
    for i in range(0, len):
        if i % 3 == 0 and i % 5 == 0:
            numeros.append(i)
    
    print(numeros)

def soma_de_digitos():
    num = int(input("Digite um número: "))

    soma = 0
    while num > 0:
        digito = num % 10
        soma += digito
        num //= 10
    
    print(f"A soma dos dígitos é: {soma}")
    
soma_de_digitos()
    
    

    
    

    