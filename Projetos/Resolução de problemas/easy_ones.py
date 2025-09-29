def int_float_inputs():
    int_num = int(input("Digite um número: "))
    float_num = float(input("Digite outro número: "))

    result = round(int_num * float_num)
    print(result)
    
def math_power():
    base_num = int(input("Digite um número: "))
    power_num = int(input("Digite outro número: "))

    result = base_num ** power_num
    print(result)

import random   
def random_number():
    random_num = random.randint(1, 100)
    print(random_num)

def floor_division():
    num1 = int(input("Digite um número: "))
    num2 = int(input("Digite outro número: "))

    result = num1 // num2
    print(result)