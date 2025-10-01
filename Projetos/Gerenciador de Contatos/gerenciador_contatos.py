agenda = []

def adicionar_contato(nome, telefone, email):
    """Adiciona um novo contato á agenda."""
    contato = {"nome": nome,
               "telefone": telefone,
               "email": email}
    agenda.append(contato)
    print(f"Contato {nome} adicionado com sucesso!")

def editar_contato(nome_antigo, novo_nome, novo_telefone, novo_email):
    """Edita um contato cadastrado na agenda"""

    # Variável para rastrear se encontramos o contato
    contato_encontrado = False

    for contato in agenda:
        if contato["nome"].lower() == nome_antigo.lower():
            # Atualiza os dados do contato encontrado
            contato["nome"] = novo_nome
            contato["telefone"] = novo_telefone
            contato["email"] = novo_email

            # Marca que o contato foi encontrado
            contato_encontrado = True

            # Adiciona o 'break' para parar o loop após encontrar e editar o primeiro contato.
            # Isso evita editar contatos duplicados acidentalmente.
            break

    # a mensagem de sucesso ou erro é exibida com base na variável de controle
    if contato_encontrado:
        print(f"Contato '{nome_antigo}' alterado com sucesso para '{novo_nome}'!")
    else:
        print(f"Erro: Contato com o nome '{nome_antigo}' não foi encontrado.")

def buscar_contato(nome_busca):
    """Busca um contato na agenda pelo nome."""
    encontrados = []
    for contato in agenda:
        if nome_busca.lower() in contato["nome"].lower():
            encontrados.append(contato)

    if not encontrados:
        print(f"Nenhum contato encontrado com o nome '{nome_busca}'.")
    else:
        print("=== Contatos encontrados ===")
        for contato in encontrados:
            print(f"Nome: {contato['nome']}, Telefone: {contato['telefone']}, Email: {contato['email']}")

def listar_contatos():
    """Exibe todos os contatos da agenda."""
    print("=== Todos os contatos ===")
    if not agenda:
        print("A agenda está vazia.")
    else:
        for indice, contato in enumerate(agenda):
            print(f"{indice + 1}. Nome: {contato['nome']}, Telefone: {contato['telefone']}, Email: {contato['email']}")

def menu_principal():
    """Exibe o menu principal e gerencia a escolha do usuário."""
    print("=== Bem vindo ao Gerenciador de Contatos ===")
    while True:
        print("Opções:")
        print("1. Adicionar contato")
        print("2. Editar contato")
        print("3. Buscar contato")
        print("4. Listar todos os contatos")
        print("5. Sair")

        escolha = input("Digite o número da opção desejada: ")

        if escolha == '1':
            nome = input("Nome do contato: ")
            telefone = input("Telefone do contato: ")
            email = input("Email do contato: ")
            adicionar_contato(nome, telefone, email)
        elif escolha == '2':
            nome_antigo = input("Digite o nome para editar o contato: ")
            novo_nome = input("Novo nome do contato: ")
            novo_telefone = input("Novo telefone do contato: ")
            novo_email = input("Novo email do contato: ")
            editar_contato(nome_antigo,novo_nome, novo_telefone, novo_email)
        elif escolha == '3':
            nome_busca = input("Digite o nome para buscar: ")
            buscar_contato(nome_busca)
        elif escolha == '4':
            listar_contatos()
        elif escolha == '5':
            print("Saindo do programa. Até mais!")
            break
        else:
            print("Opção inválida.")

# --- Início do Programa ---
menu_principal()