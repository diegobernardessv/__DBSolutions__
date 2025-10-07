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

provedores = []

for email in emails:
    provedor = email.split('@')[-1]
    provedores.append(provedor)

print("--- Lista de Provedores de Email ---")
# Usando enumerate para obter o índice (começando em 1) e o provedor
for indice, provedor in enumerate(provedores, start=1):
    # Imprime o número do item, seguido pelo provedor com a primeira letra maiúscula
    print(f"{indice}. {provedor.capitalize()}")
    
print("=== 5 provedores mais comuns===")
recorrencia = {}
for provedor in provedores:
    if provedor in recorrencia:
        recorrencia[provedor] += 1
    else:
        recorrencia[provedor] = 1
        
# 1. Ordenar os itens do dicionário pela contagem (o segundo elemento da tupla, item[1]), em ordem decrescente.
provedores_ordenados = sorted(recorrencia.items(), key=lambda item: item[1], reverse=True)

# 2. Iterar sobre a lista já ordenada e imprimir os resultados.
# Usamos um slice [:5] para pegar apenas os 5 primeiros.
for indice, (provedor, contagem) in enumerate(provedores_ordenados[:5], start=1):
    print(f"{indice}. {provedor.capitalize()}: {contagem} emails")


    
