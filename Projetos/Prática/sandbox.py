nomes = ["Diego", "Fernanda", "Carro", "Marcio", "Sol", "Lua", "Moai", "Robson", "Camelo"]

lista_ordenada = sorted(nomes)
print(nomes)
print(lista_ordenada)

nomes.sort()
print(nomes)

nomes.sort(reverse=True)
print(nomes)

contagem = len(nomes)
print(contagem)

print("=== Lista de presença ===\n")
for i, nome in enumerate(nomes):
    print(f"{i + 1}. {nome}")