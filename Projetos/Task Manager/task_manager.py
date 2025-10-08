todos = []

while True:
    user_action = input("Type add, edit, show, or exit: ")
    user_action = user_action.strip()

    match user_action:
        case 'add':
            todo = input("Enter a todo: ")
            todos.append(todo)
        case 'edit':
            number = int(input("Number of the todo to edit: "))
            number = number - 1
            new_todo = input("Enter a new todo: ")
            todos[number] = new_todo
        case 'show':
            for indice, item in enumerate(todos):
                tarefa = f"{indice + 1}. {item}"
                print(tarefa)
        case 'clear':
            todos.clear()
        case 'exit':
            break
print("Bye!")


