def calculadora_de_gorjeta():
    print(''' _____________________
|  _________________  |
| | JO  3.141592654 | |
| |_________________| |
|  __ __ __ __ __ __  |
| |__|__|__|__|__|__| |
| |__|__|__|__|__|__| |
| |__|__|__|__|__|__| |
| |__|__|__|__|__|__| |
| |__|__|__|__|__|__| |
| |__|__|__|__|__|__| |
|  ___ ___ ___   ___  |
| | 7 | 8 | 9 | | + | |
| |___|___|___| |___| |
| | 4 | 5 | 6 | | - | |
| |___|___|___| |___| |
| | 1 | 2 | 3 | | x | |
| |___|___|___| |___| |
| | . | 0 | = | | / | |
| |___|___|___| |___| |
|_____________________|''')
    
    print(" ")
    
    print("Bem vindo ao calculador de gorjeta!")
    print(" ")
    
    conta = float(input("Qual foi o valor total da conta? R$ "))
    total_pessoas = int(input("Quantas pessoas vão dividir a conta? "))
    gorjeta = int(input("Qual a porcentagem da gorjeta? 10, 12 ou 15(%)? "))
    
    valor_total = gorjeta / 100 * conta + conta
    valor_por_pessoa = valor_total / total_pessoas
      
    print(f"Cada pessoa deve pagar: R${valor_por_pessoa:.2f}")
    
calculadora_de_gorjeta()