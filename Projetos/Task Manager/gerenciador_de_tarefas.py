tarefas = []

while True:
    user_action = input("Digite add, mostrar, editar, excluir ou sair: ")
    user_action = user_action.strip()

    match user_action:
        case 'add':
            tarefa = input("Digite uma tarefa: ")
            tarefas.append(tarefa)
        case 'mostrar':
            for index, tarefa in enumerate(tarefas):
                listar_tarefa = f"{index + 1}. {tarefa}"
                print(listar_tarefa)
        case 'editar':
            numero = int(input("Digite o número da tarefa que deseja editar: "))
            tarefa = input("Digite a nova tarefa: ")
            tarefas[numero - 1] = tarefa
        case 'excluir':
            numero = int(input("Digite o número da tarefa que deseja excluir: "))
            tarefas.pop(numero - 1)
        case 'sair':
            break
print("Até mais!")