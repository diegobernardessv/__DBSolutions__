def manipular_lista(numeros):
    if len(numeros) < 2:
        return None
    lista = []
    tamanho = int(input("Digite o tamanho da lista: "))

    for i in range(0, tamanho):
        elemento = int(input("Digite um elemento: "))
        lista.append(elemento)

    # Soma dos elementos
    soma = sum(lista)
    print(f"A soma dos elementos é: {soma}")

    # Maior número da lista
    maior_num = max(lista)
    print(f"O maior número da lista é {maior_num}")

    lista.sort(reverse=True)
    print(lista)



manipular_lista()


