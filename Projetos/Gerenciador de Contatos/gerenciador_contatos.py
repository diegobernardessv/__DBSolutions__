agenda = []

def adicionar_contato(nome, telefone, email):
    """Adiciona um novo contato á agenda."""
    contato = {"nome": nome,
               "telefone": telefone,
               "email": email}
    agenda.append(contato)
    print(f"Contato {nome} adicionado com sucesso!")

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
        print("2. Buscar contato")
        print("3. Listar todos os contatos")
        print("4. Sair")

        escolha = input("Digite o número da opção desejada: ")

        if escolha == '1':
            nome = input("Nome do contato: ")
            telefone = input("Telefone do contato: ")
            email = input("Email do contato: ")
            adicionar_contato(nome, telefone, email)
        elif escolha == '2':
            nome_busca = input("Digite o nome para buscar: ")
            buscar_contato(nome_busca)
        elif escolha == '3':
            listar_contatos()
        elif escolha == '4':
            print("Saindo do programa. Até mais!")
            break
        else:
            print("Opção inválida.")

# --- Início do Programa ---
menu_principal()