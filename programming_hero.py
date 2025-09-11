def multiply_numbers():
    int_num1 = int(input('Digite o primeiro número: '))
    float_num2 = float(input('Digite o segundo número: '))
    result = int_num1 * float_num2
    
    print(f"O resultado da multiplicação é: {result}.")
    
def math_power():
    int_num = int(input('Digite um número: '))
    int_power = int(input('Digite a potência: '))
    
    result1 = int_num ** int_power
    result2 = pow(int_num, int_power)
    
    print(f"O resultado da potência é {result1}.")
    print(f"O resultado da potência é {result2}.")
    
import random

def random_number():
    random_number = random.randint(1, 100)
    print(f"O número aleatório é {random_number}.")
    
import math

def floor_division():
    num1 = int(input('Digite o primeiro número: '))
    num2 = int(input('Digite o segundo número: '))
    
    result1 = num1 // num2
    result2 = math.floor(num1 / num2)
    
    print(f"O resultado da divisão é {result1}.")
    
def swap_variables():
    var1 = input('Digite o primeiro valor: ')
    var2 = input('Digite o segundo valor: ')
    
    var1, var2 = var2, var1
    
    print(f"O primeiro valor é {var1}.")
    print(f"O segundo valor é {var2}.")
    
def max_of_two():
    num1 = int(input("Digite o primeiro número: "))
    num2 = int(input("Digite o segundo número: "))
    
    largest = max(num1, num2)
    
    print(f"O maior número é {largest}.")
    
def max_of_three():
    num1 = int(input("Digite o primeiro número: "))
    num2 = int(input("Digite o segundo número: "))
    num3 = int(input("Digite o terceiro número: "))
    
    largest = max(num1, num2, num3)
    
    print(f"O maior número é {largest}.")
    
def average_of_numbers():
    total_numbers = int(input("Quantos números você quer analisar? "))
    numbers = []
    
    for i in range(0, total_numbers):
        number = int(input("Insira um número: "))
        numbers.append(number)
    
    soma = sum(numbers)
    average1 = soma / total_numbers
    print(f"A média dos números escolhidos é {average1}.")
    
def divisible_by_3and5(num):
    result = []

    for i in range(num):
        if i % 3 == 0 and i % 5 == 0:
            result.append(i)

    print(f"Os números divisiveis por 3 e 5 até {num} são: {result}")

def soma_de_digitos():
    numero = input("Digite um número: ")
    
    soma = 0
    
    for digito in numero:
        soma += int(digito)
    
    print(f"A soma dos dígitos de {numero} é {soma}.")
    
soma_de_digitos()   