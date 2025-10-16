checagem = True
numero = int(input("Digite um número: \n"))

while checagem:
    if numero % 2 == 0:
        print(f"O número {numero} é par.")
    else:
        print(f"O número {numero} é ímpar.")

    resposta_certa = False
    while not resposta_certa:
        repetir_checagem = input("Deseja checar novamente? (s/n) \n").lower()
        if repetir_checagem == "s":
            numero = int(input("Digite um número: \n"))
            resposta_certa = True
        elif repetir_checagem == "n":
            print("Até a próxima!")
            resposta_certa = True
            checagem = False
        else:
            print("Opção inválida.")