print("Seja bem vindo á Calculadora de Gorjeta!")
conta = float(input("Qual foi o valor total da conta? R$ \n"))
porcentagem_gorjeta = int(input("Qual porcentagem de gorjeta gostaria de dar? 10%, 12% ou 15%? \n"))
quantidade_pessoas = int(input("Quantas pessoas vão dividir a conta? \n"))

calculo_conta = round(150 / 5 * 1.12, 2)
print(f"Cada pessoa deve pagar: R$ {calculo_conta} reais.")


