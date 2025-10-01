agenda = []

print("=== Bem vindo ao seu Gerenciador de Contatos ===")

while True:
    print("\nOpções:")
    print("1. Adicionar contato")
    print("2. Buscar contato por nome")
    print("3. Listar todos os contatos")
    print("4. Sair")

    escolha = input("Digite o número da opção desejada: ")

    if escolha == "1":
        nome = input("Nome do contato: ")
        telefone = input("Telefone do contato: ")
        email = input("Email do contato: ")
        contato = {"nome": nome, "telefone": telefone, "email": email}
        agenda.append(contato)
        print(f"Contato {nome} adicionado com sucesso!")

    elif escolha == "2":
        nome_busca = input("Digite o nome do contato que deseja buscar: ")
        encontrado = False
        for contato in agenda:
            if nome_busca.lower() in contato["nome"].lower():
                print("\n--- Contato Encontrado ---")
                print(f"Nome: {contato['nome']}")
                print(f"Telefone: {contato['telefone']}")
                print(f"Email: {contato['email']}")
                encontrado = True

        if not encontrado:
            print(f"Nenhum contato encontrado com o nome {nome_busca}.")

    elif escolha == "3":
        print("=== Todos os contatos ===")
        if not agenda:
            print("A agenda está vazia.")
        else:
            for i, contato in enumerate(agenda):
                print(f"{i + 1}. Nome: {contato['nome']}, Telefone: {contato['telefone']}, Email: {contato['email']}")

    elif escolha == "4":
        print("Obrigado por usar o Gerenciador de Contatos. Até logo!")
        break

    else:
        print("Opção inválida.")