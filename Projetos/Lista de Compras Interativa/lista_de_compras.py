lista_de_compras = []

print("--- Bem-vindo à sua Lista de Compras Interativa! ---")

while True:
    print("\nOpções:")
    print("1. Adicionar item")
    print("2. Remover item")
    print("3. Ver lista")
    print("4. Sair")

    escolha = input("Digite o número da opção desejada: ")

    if escolha == "1":
        item = input("Qual item você deseja adicionar: ")
        lista_de_compras.append(item)
    elif escolha == "2":
        item = input("Qual item você deseja remover: ")
        if item in lista_de_compras:
            lista_de_compras.remove(item)
        else:
            print(f"O item '{item}' não foi encontrado na lista.")
    elif escolha == "3":
        print("\n--- Sua Lista de Compras ---")
        if not lista_de_compras: # Checa se a lista está vazia
            print("A lista está vazia.")
        else:
            # Usando 'for' com 'enumerate' para obter o índice e o item
            for i, item in enumerate(lista_de_compras):
                print(f"{i + 1}. {item}")
    elif escolha == "4":
        print("Obrigado por usar a lista de compras. Até logo!")
        break
    else:
        print("Opção inválida. Tente novamente.")

