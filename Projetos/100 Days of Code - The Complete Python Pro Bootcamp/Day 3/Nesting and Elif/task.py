print("=== Bem vindo á Montanha Russa Sombria! ===\n")
altura = int(input("Qual é a sua altura em centímetros? "))

if altura >= 120:
    print("Você pode andar na Montanha Russa!\n")

    idade_validada = False
    # Validação da idade
    while not idade_validada:
        idade = int(input("Qual é a sua idade? "))

        if idade < 1 or idade > 100:
            print("Opção inválida. Por favor, insira uma idade entre 1 e 100.")
        # Lógica de preços para idades válidas
        elif idade <= 12:
            print("Você deve pagar $5.")
            idade_validada = True
        elif idade <= 18:
            print("Você deve pagar $7.")
            idade_validada = True
        else:  # Idade maior que 18 e válida
            print("Você deve pagar $12.")
            idade_validada = True
else:
    print("Desculpe. Você precisa ficar mais alto para andar na montanha russa!")
