import collections

emails = [
    "alicia@gmail.com", "pedro@globo.com", "sofia@gmail.com", "gabriel@outlook.com", "luisasantosv@gmail.com",
    "roberta@gmail.com", "marcelina@globo.com", "carloshenrique@gmail.com", "beatriz@outlook.com", "miguel@gmail.com",
    "tiago@uol.com", "vitoria@infratec.com.br", "davi.pereira@yahoo.com", "elena.gomes@hotmail.com",
    "joana.almeida@bol.com.br", "alex.martins@ig.com.br", "camila.souza@outlook.com",
    "ricardo.ferreira@gmail.com", "patricia.lima@terra.com.br", "sergio.ribeiro@protonmail.com",
    "adriana.carvalho@icloud.com", "bernardo.fernandes@aol.com", "amand.silveira@zohomail.com",
    "raul.machado@gmx.com", "fernando.barbosa@yandex.com", "isabela.azevedo@mail.com",
    "felipe.dias@fastmail.com", "tatiana.fonseca@tutanota.com", "guilherme.vieira@mailfence.com",
    "heloisa.nunes@runbox.com", "caue.freitas@posteo.de", "julia.moraes@disroot.org",
    "luan.vasconcelos@riseup.net", "mariana.queiroz@autistici.org", "nicolas.castro@systemli.org",
    "olivia.lopes@openmailbox.org", "paulo.santana@countermail.com", "quintana.santos@kolabnow.com",
    "renan.goncalves@scryptmail.com", "talita.ramos@lavabit.com", "vinicius.correia@cock.li",
    "wendy.cordeiro@startmail.com", "yago.aguiar@privatemail.com", "zoraide.monteiro@airmail.cc",
    "artur.batista@inbox.com", "bruna.pinheiro@mail.ru", "cesar.campos@seznam.cz",
    "debora.nascimento@onet.pl", "eloi.siqueira@daum.net", "florinda.dantas@naver.com",
    "george.sales@web.de", "hannah.bitencourt@wp.pl", "ivone.valente@abv.bg",
    "jorge.medeiros@mail.bg", "karen.roch@ukr.net", "leo.lemos@rambler.ru",
    "maya.braga@bk.ru", "nelson.melo@list.ru", "ofelia.figueiredo@km.ru",
    "pablo.neves@sapo.pt", "quezia.domingos@terra.es", "rodrigo.duarte@netvigator.com",
    "samara.alves@charter.net", "teresa.barreto@comcast.net", "ulisses.couto@verizon.net",
    "vanessa.lima@att.net", "washington.azevedo@sbcglobal.net", "xiomara.dias@bellsouth.net",
    "yago.fonseca@rogers.com", "zilda.vieira@shaw.ca", "antonio.nunes@telus.net",
    "eliane.freitas@virginmedia.com", "gilberto.moraes@btinternet.com", "helena.vasconcelos@ntlworld.com",
    "osmar.queiroz@o2.co.uk", "patricia.castro@tiscali.co.uk", "ronaldo.lopes@talktalk.net",
    "sandra.santana@orange.fr", "tiago.santos@free.fr", "ubirajara.goncalves@bbox.fr",
    "vivian.ramos@laposte.net", "william.correia@gmx.fr", "xavier.cordeiro@laposte.net",
    "yuri.aguiar@orange.es", "zeca.monteiro@telefonica.es", "aline.batista@libero.it",
    "bruno.pinheiro@tin.it", "clara.campos@alice.it", "davi.nascimento@poste.it",
    "emily.siqueira@virgilio.it", "francisco.dantas@vodafone.it", "geovana.sales@tiscali.it",
    "hermando.bitencourt@fastwebnet.it", "isabel.valente@email.it", "joel.medeiros@aruba.it",
    "karla.roch@tim.it", "lucas.lemos@email.cz", "marcia.braga@web.de",
    "nicolas.melo@mail.ch", "olavo.figueiredo@hispeed.ch", "paola.neves@bluewin.ch",
    "quiteria.domingos@sunrise.ch", "raquel.duarte@sunrise.ch", "sandra.alves@gmx.ch",
    "tomas.barreto@mail.at", "ursula.couto@gmx.at", "vanessa.lima@aon.at",
    "washington.azevedo@utanet.at", "xiomara.dias@chello.at", "yago.fonseca@inode.at",
    "zilda.vieira@kabsi.at", "artur.nunes@mail.be", "beatriz.freitas@skynet.be",
    "caio.moraes@telenet.be", "diana.vasconcelos@proximus.be", "enzo.queiroz@vlaanderen.be",
    "flavia.castro@wallonie.be", "guilherme.lopes@brussels.be", "helena.santana@mail.nl",
    "igor.santos@ziggo.nl", "julia.goncalves@upcmail.nl", "kaua.ramos@xs4all.nl",
    "laura.correia@kpnmail.nl", "matheus.cordeiro@telfort.nl", "nicole.aguiar@online.nl",
    "pedro.monteiro@casema.nl", "quiteria.batista@zeelandnet.nl", "ricardo.pinheiro@planet.nl",
    "sabrina.campos@chello.nl", "tiago.nascimento@home.nl", "ursula.siqueira@wanadoo.nl",
    "victor.dantas@zonnet.nl", "wanderley.sales@zonnet.nl", "xavier.bitencourt@worldonline.nl",
    "yara.valente@mail.dk", "zeca.medeiros@tdc.dk", "alessandra.roch@post.dk",
    "bernardo.lemos@mail.no", "cecilia.braga@online.no", "david.melo@getmail.no",
    "elisa.figueiredo@mail.se", "fabricio.neves@bredband.net", "giselle.domingos@tele2.se",
    "henrique.duarte@comhem.se", "ivone.alves@bahnhof.se", "jonas.barreto@glocalnet.se",
    "karina.couto@passagen.se", "lucas.costa@swipnet.se", "monica.pereira@telia.se",
    "nelson.santos@spray.se", "olivia.araujo@mail.fi", "paulo.gomes@elisa.fi",
    "quintino.fernandes@saunalahti.fi", "rosana.silva@dnainternet.fi", "sergio.souza@kolumbus.fi",
    "tania.rodrigues@welho.fi", "ubirajara.ferreira@sonera.fi", "vera.martins@mail.pl",
    "wagner.almeida@wp.pl", "xenia.ribeiro@o2.pl", "yuri.oliveira@onet.pl",
    "zilda.carvalho@interia.pl", "adam.martinez@gazeta.pl", "brenda.lopes@poczta.fm",
    "claudio.silva@spoko.pl", "darlene.castro@autograf.pl", "elias.pereira@home.pl",
    "fatima.almeida@g.pl", "gustavo.machado@konto.pl", "helena.rodrigues@poczta.onet.pl",
    "isaac.fernandes@poczta.fm", "janice.gomes@gazeta.pl", "kelvin.lima@home.pl",
    "lorena.santos@poczta.onet.pl", "marcelo.azevedo@poczta.fm", "nadia.dias@gazeta.pl",
    "osmar.fonseca@home.pl", "paloma.vieira@poczta.onet.pl", "quentin.nunes@poczta.fm",
    "raquel.freitas@gazeta.pl", "salvador.moraes@home.pl", "talita.vasconcelos@poczta.onet.pl",
    "ubiratan.queiroz@poczta.fm", "valeria.castro@gazeta.pl", "walter.lopes@home.pl",
    "xenia.santana@poczta.onet.pl", "yago.santos@poczta.fm", "zaira.goncalves@gazeta.pl",
    "aline.ramos@home.pl", "bruno.correia@poczta.onet.pl", "carol.cordeiro@poczta.fm",
    "davi.aguiar@gazeta.pl", "emilly.monteiro@home.pl", "felippe.batista@poczta.onet.pl",
    "gisele.pinheiro@poczta.fm", "hugo.campos@gazeta.pl", "ingrid.nascimento@home.pl",
    "joao.siqueira@poczta.onet.pl", "karen.dantas@poczta.fm", "leandro.sales@gazeta.pl",
    "monique.bitencourt@home.pl", "natan.valente@poczta.onet.pl", "olga.medeiros@poczta.fm",
    "patrick.roch@gazeta.pl", "quiteria.lemos@home.pl", "roberto.braga@poczta.onet.pl",
    "simone.melo@poczta.fm", "teodoro.figueiredo@gazeta.pl", "ursula.neves@home.pl",
    "vinicius.domingos@poczta.onet.pl", "wendy.duarte@poczta.fm", "xenia.alves@gazeta.pl",
    "yuri.barreto@home.pl", "zilda.couto@poczta.onet.pl", "andre.lima@poczta.fm",
    "bianca.azevedo@gazeta.pl", "carlos.dias@home.pl", "debora.fonseca@poczta.onet.pl",
    "emerson.vieira@poczta.fm", "flavia.nunes@gazeta.pl"
]

# Extrair apenas a parte do provedor de cada e-mail
lista_provedores = [email.split("@")[1] for email in emails]

# Contar a frequência de cada provedor
contagem = collections.Counter(lista_provedores)

print("=== Lista com os 5 provedores de e-mail mais comuns ===")

# Usa enumerate() para criar um índice (ranking) para cada item da lista
# O método .most_common(argumento) já retorna os mais frequentes, ordenados do maior para o menor
for indice, (provedor, quantidade) in enumerate(contagem.most_common(5)):
    print(f"{indice + 1}°: {provedor} - {quantidade} e-mails.")






