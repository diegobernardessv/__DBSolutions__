'''Imagine que você é um cientista olhando para um novo tipo de célula sob o microscópio.
Este tipo de célula se divide em 2 células filhas a cada 24 horas,
o que significa que a população de células duplica todos os dias.'''

# === Tarefa ===
'''Complete o código para pegar a população inicial de células e o número de dias
que você está observando as células para calcular a população de células no final de cada dia.'''

# pegar a população celular inicial como input
celulas = int(input("Digite a população inicial de células: "))

# pegar o número de dias como input
dias = int(input("Digite o número de dias: "))

# Iniciar o contador de dias
dia_atual = 1

# Loop while
while dia_atual <= dias:
    celulas = celulas * 2
    
    # Mensagem diária
    print(f"Dia {dia_atual}: {celulas} células.")
    dia_atual += 1