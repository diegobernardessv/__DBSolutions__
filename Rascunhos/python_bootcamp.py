def multiply_numbers():
    int_num1 = int(input('Digite o primeiro número: '))
    float_num2 = float(input('Digite o segundo número: '))
    result = int_num1 * float_num2
    
    print(f"O resultado da multiplicação é: {result}.")
    
def math_power():
    int_num = int(input('Digite um número: '))
    int_power = int(input('Digite a potência: '))
    
    result1 = int_num ** int_power
    result2 = pow(int_num, int_power)
    
    print(f"O resultado da potência é {result1}.")
    print(f"O resultado da potência é {result2}.")
    
import random

def random_number():
    random_number = random.randint(1, 100)
    print(f"O número aleatório é {random_number}.")
    
import math

def floor_division():
    num1 = int(input('Digite o primeiro número: '))
    num2 = int(input('Digite o segundo número: '))
    
    result1 = num1 // num2
    result2 = math.floor(num1 / num2)
    
    print(f"O resultado da divisão é {result1}.")
    
def swap_variables():
    var1 = input('Digite o primeiro valor: ')
    var2 = input('Digite o segundo valor: ')
    
    var1, var2 = var2, var1
    
    print(f"O primeiro valor é {var1}.")
    print(f"O segundo valor é {var2}.")
    
def max_of_two():
    num1 = int(input("Digite o primeiro número: "))
    num2 = int(input("Digite o segundo número: "))
    
    largest = max(num1, num2)
    
    print(f"O maior número é {largest}.")
    
def max_of_three():
    num1 = int(input("Digite o primeiro número: "))
    num2 = int(input("Digite o segundo número: "))
    num3 = int(input("Digite o terceiro número: "))
    
    largest = max(num1, num2, num3)
    
    print(f"O maior número é {largest}.")
    
def average_of_numbers():
    total_numbers = int(input("Quantos números você quer analisar? "))
    numbers = []
    
    for i in range(0, total_numbers):
        number = int(input("Insira um número: "))
        numbers.append(number)
    
    soma = sum(numbers)
    average1 = soma / total_numbers
    print(f"A média dos números escolhidos é {average1}.")
    
def divisible_by_3and5(num):
    result = []

    for i in range(num):
        if i % 3 == 0 and i % 5 == 0:
            result.append(i)

    print(f"Os números divisiveis por 3 e 5 até {num} são: {result}")

def soma_de_digitos():
    numero = input("Digite um número: ")
    
    soma = 0
    
    for digito in numero:
        soma += int(digito)
    
    print(f"A soma dos dígitos de {numero} é {soma}.")

def ano_bissexto():
    ano = input("Qual ano você quer checar? ")
    ano_num = int(ano)

    if ano_num % 4 == 0:
        print(f"{ano_num} é um ano bissexto.")
    else:
        print(f"{ano_num} não é um ano bissexto.")

def num_power():
    base_num = int(input("Enter a number: "))
    power_num = int(input("Enter another number: "))

    result = pow(base_num, power_num)

    print(f"Your result is {result}")

def band_name_generator():
    print("Welcome to the Band Name Generator.")

    city = input("What's the name of the city you grew up? ")
    pet = input("What's the name of your favorite pet? ? ")

    print(f"Your band name could be {city} {pet}")

def calculadora_imc():
    altura = float(input("Qual é a sua altura em metros? "))
    peso = float(input("Qual é o seu peso em kilo? "))

    imc = peso / (altura * altura)
    print(f"Seu IMC é {imc}")

    if imc < 18.5:
        print("-----")
        print("Você está abaixo do peso.")
    elif 18.5 <= imc < 25:
        print("-----")
        print("Parabéns! Você está saudável.")
    elif 25 <= imc <= 30:
        print("-----")
        print("Você está com sobrepeso.")
    else:
        print("-----")
        print("Você precisa praticar atividade física. Você está obeso.")

def contagem_palavras():
    profile = input("Escreva sobre você: ")

    contagem = 0
    for letra in profile:
        if letra == " ":
            contagem += 1
    contagem += 1

    print(contagem)

def contar_vogais(texto):
    vogais = ['a', 'e', 'i', 'o', 'u', 'á','é','í','ó','ú']
    contagem = 0

    texto_lower = texto.lower()

    for letra in texto_lower:
        if letra in vogais:
            contagem += 1
    return contagem

def fibonacci_series(numbers):
    list = [0,1]
    while len(list) < 500:
        list.append(list[-1] + list[-2])

    return list

def user_input():

    int_num = int(input("Digite um número inteiro: "))
    float_num = float(input("Digite um número real: "))

    result = int_num * float_num
    print(f"The result of {int_num} multiplied by {float_num} is {result}")

def tabela_periodica(n):
    i = 1
    print(f"=== Tabela periódica do nº {n} ===\n")
    while i <= 10:
        print(f"{n} x {i} = {n*i}")
        i += 1
    print('')

# Cria outra lista somente com nomes únicos
def nova_lista(lista_completa):
    lista = []
    # Percorre a lista 'nomes' para adicionar somente nomes únicos
    for nome in lista_completa:
        if nome not in lista:
            lista.append(nome)
    return lista
# Lista de nomes inicial
nomes = [
    "Maria", "João", "Ana", "Pedro", "Maria", "Lucas", "Maria", "Ana", "Sofia", "João",
    "Maria", "Gabriel", "Julia", "Pedro", "Lucas", "João", "Maria", "Sofia", "Ana", "Gabriel",
    "João", "Lucas", "Julia", "Maria", "Sofia", "Pedro", "João", "Ana", "Gabriel", "Lucas",
    "Maria", "João", "Sofia", "Pedro", "Julia", "Ana", "Gabriel", "Maria", "Lucas", "João",
    "Sofia", "Ana", "Pedro", "Julia", "Gabriel", "Maria", "João", "Lucas", "Sofia", "Ana",
    "Pedro", "Maria", "Julia", "Gabriel", "João", "Lucas", "Sofia", "Ana", "Pedro", "Maria",
    "Julia", "Gabriel", "João", "Lucas", "Sofia", "Ana", "Pedro", "Maria", "Julia", "Gabriel",
    "João", "Lucas", "Sofia", "Ana", "Pedro", "Maria", "Julia", "Gabriel", "João", "Lucas",
    "Sofia", "Ana", "Pedro", "Maria", "Julia", "Gabriel", "João", "Lucas", "Sofia", "Ana",
    "Pedro", "Maria", "Julia", "Gabriel", "João", "Lucas", "Sofia", "Ana", "Pedro", "Maria",
    "Julia", "Gabriel", "João", "Lucas", "Sofia", "Ana", "Pedro", "Maria", "Julia", "Gabriel",
    "João", "Lucas", "Sofia", "Ana", "Pedro", "Maria", "Julia", "Gabriel", "João", "Lucas",
    "Sofia", "Ana", "Pedro", "Maria", "Julia", "Gabriel", "João", "Lucas", "Sofia", "Ana",
    "Pedro", "Maria", "Julia", "Gabriel", "João", "Lucas", "Sofia", "Ana", "Pedro", "Maria",
    "Julia", "Gabriel", "João", "Lucas", "Sofia", "Ana", "Pedro", "Maria", "Julia", "Gabriel",
    "João", "Lucas", "Sofia", "Ana", "Pedro", "Maria", "Julia", "Gabriel", "João", "Lucas",
    "Sofia", "Ana", "Pedro", "Maria", "Julia", "Gabriel", "João", "Lucas", "Sofia", "Ana",
    "Pedro", "Maria", "Julia", "Gabriel", "João", "Lucas", "Sofia", "Ana", "Pedro", "Maria",
    "Julia", "Gabriel", "João", "Lucas", "Sofia", "Ana", "Pedro", "Maria", "Julia", "Gabriel",
    "João", "Lucas", "Sofia", "Ana", "Pedro", "Maria", "Julia", "Gabriel", "João", "Lucas"
]

# Cria nova lista somente com números únicos
def remover_duplicados(numeros):
    lista_unicos = []
    # Percorre a lista
    for numero in numeros:
        if numero not in lista_unicos:
            lista_unicos.append(numero)
    print(lista_unicos)
# Lista de números inicial
numeros = [22,11,3,1,4,5,5,2,2,11,66,89]

def max_number_between2():
    num1 = int(input("Insira um numero: "))
    num2 = int(input("Insira outro numero: "))

    largest = max(num1, num2)

    print(f"The largest number is {largest}")

def max_number_between3():
    print("Por favor, insira 3 números:")
    print("")
    num1 = int(input("Primeiro número: "))
    num2 = int(input("Segundo número: "))
    num3 = int(input("Terceiro número: "))

    largest = max(num1, num2, num3)

    print(f"The largest number is {largest}")

def average_numbers():
    total_numbers = int(input("Quantos números você quer analisar? "))
    numbers = []
    for i in range(0, total_numbers):
        number = float(input("Insira um numero: "))
        numbers.append(number)

    average = sum(numbers) / total_numbers
    print(f"A média dos números escolhidos é {average}")
    
def divisible_by_3and5():
    num = int(input("Insira um número: "))

    result = []
    
    for i in range(num):
        if i % 3 == 0 and i % 5 == 0:
            result.append(i)
    
    print(f"Os números divisíveis por 3 e 5 até {num} são: {result}")

# Soma de digitos de um valor
def soma_de_digitos(numero):
    num = input("Enter a number: ")
    soma = 0
    for digito in num:
        soma += int(digito)

# Dicionário de uma lista de compras
def lista_de_compras():
    compras = {
        1: "arroz",
        2: "feijão",
        3: "macarrão",
        4: "carne",
        5: "leite",
        6: "ovos",
        7: "batata",
    }

    # Itera sobre todos os valores do dicionário
    for value, key in compras.items():
        print(f"{value}: {key}")

# Dicionário de uma lista de convidados
def lista_de_convidados():
    convidados = {
        1: "João",
        2: "Maria",
        3: "Pedro",
        4: "Ana",
        5: "Lucas",
        6: "Sofia",
        7: "Carlos",
        8: "Jill",
        9: "Diego",
        10: "Julia"
    }
    
    convidados[11] = "Marcos Fernando"
    convidados[12] = "Corvo"
    
    # Lista todas as keys do dicionário
    listagem = convidados.keys()
    
    # Itera sobre todos os valores do dicionário    
    for value, key in convidados.items():
        print(f"{value}: {key}")
        
def split_provedores():
    emails = [
    "fernando@gmail.com", "jose@globo.com", "maria@gmail.com", "cristiane@outlook.com", "diegobernardessv@gmail.com",
    "fernanda@gmail.com", "josefina@globo.com", "mariajulia@gmail.com", "cristiana@outlook.com", "diego@gmail.com",
    "fernando@uol.com", "janaina@infratec.com.br", "ana.silva@yahoo.com", "bruno.costa@hotmail.com",
    "carla.santos@bol.com.br", "daniel.oliveira@ig.com.br", "eduarda.pereira@outlook.com",
    "felipe.almeida@gmail.com", "gabriela.rodrigues@terra.com.br", "hugo.ferreira@protonmail.com",
    "isabela.martins@icloud.com", "joao.souza@aol.com", "larissa.gomes@zohomail.com",
    "marcos.lima@gmx.com", "nathalia.ribeiro@yandex.com", "otavio.carvalho@mail.com",
    "paula.fernandes@fastmail.com", "rafael.silveira@tutanota.com", "sofia.machado@mailfence.com",
    "thiago.barbosa@runbox.com", "viviane.azevedo@posteo.de", "willian.dias@disroot.org",
    "xenia.fonseca@riseup.net", "yasmin.vieira@autistici.org", "arthur.nunes@systemli.org",
    "beatriz.freitas@openmailbox.org", "caio.moraes@countermail.com", "diana.vasconcelos@kolabnow.com",
    "enzo.queiroz@scryptmail.com", "flavia.castro@lavabit.com", "guilherme.lopes@cock.li",
    "helena.santana@startmail.com", "igor.santos@privatemail.com", "julia.goncalves@airmail.cc",
    "kaua.ramos@inbox.com", "laura.correia@mail.ru", "matheus.cordeiro@seznam.cz",
    "nicole.aguiar@onet.pl", "pedro.monteiro@daum.net", "quiteria.batista@naver.com",
    "ricardo.pinheiro@web.de", "sabrina.campos@wp.pl", "tiago.nascimento@abv.bg",
    "ursula.siqueira@mail.bg", "victor.dantas@ukr.net", "wanderley.sales@rambler.ru",
    "xavier.bitencourt@bk.ru", "yara.valente@list.ru", "zeca.medeiros@km.ru",
    "alessandra.roch@sapo.pt", "bernardo.lemos@terra.es", "cecilia.braga@netvigator.com",
    "david.melo@charter.net", "elisa.figueiredo@comcast.net", "fabricio.neves@verizon.net",
    "giselle.domingos@att.net", "henrique.duarte@sbcglobal.net", "ivone.alves@bellsouth.net",
    "jonas.barreto@rogers.com", "karina.couto@shaw.ca", "lucas.costa@telus.net",
    "monica.pereira@virginmedia.com", "nelson.santos@btinternet.com", "olivia.araujo@ntlworld.com",
    "paulo.gomes@o2.co.uk", "quintino.fernandes@tiscali.co.uk", "rosana.silva@talktalk.net",
    "sergio.souza@orange.fr", "tania.rodrigues@free.fr", "ubirajara.ferreira@bbox.fr",
    "vera.martins@laposte.net", "wagner.almeida@gmx.fr", "xenia.ribeiro@laposte.net",
    "yuri.oliveira@orange.es", "zilda.carvalho@telefonica.es", "adam.martinez@libero.it",
    "brenda.lopes@tin.it", "claudio.silva@alice.it", "darlene.castro@poste.it",
    "elias.pereira@virgilio.it", "fatima.almeida@vodafone.it", "gustavo.machado@tiscali.it",
    "helena.rodrigues@fastwebnet.it", "isaac.fernandes@email.it", "janice.gomes@aruba.it",
    "kelvin.lima@tim.it", "lorena.santos@email.cz", "marcelo.azevedo@web.de",
    "nadia.dias@mail.ch", "osmar.fonseca@hispeed.ch", "paloma.vieira@bluewin.ch",
    "quentin.nunes@sunrise.ch", "raquel.freitas@sunrise.ch", "salvador.moraes@gmx.ch",
    "talita.vasconcelos@mail.at", "ubiratan.queiroz@gmx.at", "valeria.castro@aon.at",
    "walter.lopes@utanet.at", "xenia.santana@chello.at", "yago.santos@inode.at",
    "zaira.goncalves@kabsi.at", "aline.ramos@mail.be", "bruno.correia@skynet.be",
    "carol.cordeiro@telenet.be", "davi.aguiar@proximus.be", "emilly.monteiro@vlaanderen.be",
    "felippe.batista@wallonie.be", "gisele.pinheiro@brussels.be", "hugo.campos@mail.nl",
    "ingrid.nascimento@ziggo.nl", "joao.siqueira@upcmail.nl", "karen.dantas@xs4all.nl",
    "leandro.sales@kpnmail.nl", "monique.bitencourt@telfort.nl", "natan.valente@online.nl",
    "olga.medeiros@casema.nl", "patrick.roch@zeelandnet.nl", "quiteria.lemos@planet.nl",
    "roberto.braga@chello.nl", "simone.melo@home.nl", "teodoro.figueiredo@wanadoo.nl",
    "ursula.neves@zonnet.nl", "vinicius.domingos@zonnet.nl", "wendy.duarte@worldonline.nl",
    "xenia.alves@mail.dk", "yuri.barreto@tdc.dk", "zilda.couto@post.dk",
    "andre.lima@mail.no", "bianca.azevedo@online.no", "carlos.dias@getmail.no",
    "debora.fonseca@mail.se", "emerson.vieira@bredband.net", "flavia.nunes@tele2.se",
    "gabriel.freitas@comhem.se", "helena.moraes@bahnhof.se", "igor.vasconcelos@glocalnet.se",
    "jessica.queiroz@passagen.se", "kevin.castro@swipnet.se", "lorena.lopes@telia.se",
    "marina.santana@spray.se", "nicolas.santos@mail.fi", "oliver.goncalves@elisa.fi",
    "pamela.ramos@saunalahti.fi", "quintino.correia@dnainternet.fi", "rafaela.cordeiro@kolumbus.fi",
    "sofia.aguiar@welho.fi", "tiago.monteiro@sonera.fi", "vivian.batista@mail.pl",
    "walter.pinheiro@wp.pl", "xenia.campos@o2.pl", "yasmin.nascimento@onet.pl",
    "zeca.siqueira@interia.pl", "amanda.dantas@gazeta.pl", "bruno.sales@poczta.fm",
    "carolina.bitencourt@spoko.pl", "daniel.valente@autograf.pl", "eduardo.medeiros@home.pl",
    "fernanda.roch@g.pl", "gabriela.lemos@konto.pl", "hugo.braga@poczta.onet.pl",
    "isabela.melo@poczta.fm", "joana.figueiredo@gazeta.pl", "kevin.neves@home.pl",
    "leticia.domingos@poczta.onet.pl", "marcelo.duarte@poczta.fm", "natalia.alves@gazeta.pl",
    "otavio.barreto@home.pl", "paula.couto@poczta.onet.pl", "rafael.lima@poczta.fm",
    "sofia.azevedo@gazeta.pl", "thiago.dias@home.pl", "viviane.fonseca@poczta.onet.pl",
    "willian.vieira@poczta.fm", "xenia.nunes@gazeta.pl", "yasmin.freitas@home.pl",
    "zeca.moraes@poczta.onet.pl", "alice.vasconcelos@poczta.fm", "bernardo.queiroz@gazeta.pl",
    "clara.castro@home.pl", "diego.lopes@poczta.onet.pl", "elisa.santana@poczta.fm",
    "felipe.santos@gazeta.pl", "giovanna.goncalves@home.pl", "helena.ramos@poczta.onet.pl",
    "igor.correia@poczta.fm", "julia.cordeiro@gazeta.pl", "kaua.aguiar@home.pl",
    "laura.monteiro@poczta.onet.pl", "matheus.batista@poczta.fm", "nicole.pinheiro@gazeta.pl",
    "pedro.campos@home.pl", "quiteria.nascimento@poczta.onet.pl", "ricardo.siqueira@poczta.fm",
    "sabrina.dantas@gazeta.pl", "tiago.sales@home.pl", "ursula.bitencourt@poczta.onet.pl",
    "victor.valente@poczta.fm", "wanderley.medeiros@gazeta.pl", "xavier.roch@home.pl",
    "yara.lemos@poczta.onet.pl", "zeca.braga@poczta.fm", "ana.melo@gazeta.pl",
    "bruno.figueiredo@home.pl", "carla.neves@poczta.onet.pl", "daniel.domingos@poczta.fm",
    "eduarda.duarte@gazeta.pl", "felipe.alves@home.pl", "gabriela.barreto@poczta.onet.pl",
    "hugo.couto@poczta.fm", "isabela.lima@gazeta.pl", "joao.azevedo@home.pl",
    "larissa.dias@poczta.onet.pl", "marcos.fonseca@poczta.fm", "nathalia.vieira@gazeta.pl",
    "otavio.nunes@home.pl", "paula.freitas@poczta.onet.pl", "rafael.moraes@poczta.fm",
    "sofia.vasconcelos@gazeta.pl", "thiago.queiroz@home.pl", "viviane.castro@poczta.onet.pl",
    "willian.lopes@poczta.fm"
]
    
    provedores = {}

    for email in emails:
        provedor = email.split("@")[1]
        if provedor in provedores:
            provedores[provedor] += 1
        else:
            provedores[provedor] = 1
    
        print(provedor)
    
    
def soma_dos_elementos():
    lista = []
    soma = 0
    
    for i in range(0, 201):
        lista.append(i)
        soma += i
    
    print(f"=== Lista completa === \n{lista}")
    print("=========================")
    print(f"Soma dos elementos: {soma}")

def convert_miles_to_km():
    miles = float(input("Digite a distância em milhas: "))
    kilometers = 1.609344
    converted = miles * kilometers

    print(f"A distância em quilômetros é: {round(converted, 2)} km.")

class Carro:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        print(f"Um carro da marca {self.marca}, modelo {self.modelo} e ano {self.ano} foi criado.")
        
meu_carro = Carro("Toyota", "Corolla", 2022)
seu_carro = Carro("Honda", "Civic", 2021)

print(f"Meu carro é um {meu_carro.marca} {meu_carro.modelo} do ano {meu_carro.ano}.")
print(f"Seu carro é um {seu_carro.marca} {seu_carro.modelo} do ano {seu_carro.ano}")
        















