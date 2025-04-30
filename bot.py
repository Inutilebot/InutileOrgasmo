import irc.client
import irc.connection
import ssl
import random
import time

# Configurazione bot
SERVER = "irc.simosnap.org"
PORT = 6697
CHANNEL = "#orgasmiinutili"
NICKNAME = "InutileOrgasmo"
PASSWORD = "Inutili2025Orgasmi"

# Domande erotiche
DOMANDE_ERO = [
    "Qual è la tua fantasia più inconfessabile?",
    "Hai mai fatto sesso in un luogo pubblico?",
    "Cosa ti eccita di più in una persona?",
    "Se potessi provare qualsiasi esperienza sessuale, quale sarebbe?",
    "Preferisci dominare o essere dominat*?",
    "Ti piacciono i giochi di ruolo erotici?",
    "Qual è la tua posizione preferita?",
    "Hai mai guardato un film porno con qualcun altro?",
    "Hai mai avuto un sogno erotico con una persona insospettabile?",
    "Hai mai fatto sexting?",
    "Qual è il tuo sex toy preferito?",
    "Qual è la tua zona erogena più sensibile?",
    "Hai mai fatto un’esperienza a tre?",
    "Ti piacciono i baci lunghi o quelli mordaci?",
    "Hai mai fatto uno spogliarello per qualcuno?",
    "Qual è la cosa più trasgressiva che hai fatto a letto?",
    "Preferisci il sesso lento o passionale?",
    "Ti piacciono le carezze leggere o i morsi?",
    "C'è qualcosa che hai sempre voluto provare ma non hai mai osato?",
    "Ti eccita più l’odore, la voce o lo sguardo?",
    "Hai mai provato il bondage?",
    "Hai mai ricevuto o fatto un massaggio erotico?",
    "Ti piace il dirty talk?",
    "Hai mai fatto sesso ascoltando musica?",
    "Hai mai avuto una cotta per un/a prof?",
    "Se potessi essere un sex symbol, chi saresti?",
    "Hai mai indossato lingerie solo per sentirti sexy?",
    "Hai mai flirtato con uno sconosciuto solo per il brivido?",
    "Ti piacciono i giochi di potere?",
    "Hai mai avuto una fantasia con una celebrità?",
    "Hai mai fatto sesso in macchina?",
    "Qual è il posto più strano dove l’hai fatto?",
    "Hai mai scritto una lettera erotica?",
    "Hai mai fatto un gioco erotico da tavolo?",
    "Ti piacciono gli occhi bendati?",
    "Hai mai fatto sesso telefonico?",
    "Hai mai usato ghiaccio o cera?",
    "Qual è il tuo ricordo erotico preferito?",
    "Hai mai usato del cibo in un contesto erotico?"
]

# Domande erotiche surreali
DOMANDE_SURR = [
    "Faresti sesso con un alieno che cambia forma a piacere?",
    "Accetteresti un’orgia in assenza di gravità?",
    "Ti ecciterebbe un robot programmato per leggere i tuoi desideri?",
    "Faresti sesso mentale se potessi fondere le menti?",
    "Ti attrarrebbe una creatura con 7 braccia e 3 lingue?",
    "Cosa proveresti se facessi sesso in sogno con un dio?",
    "Accetteresti un invito in una dimensione erotica parallela?",
    "Se potessi trasformarti in un profumo, quale aroma seducente saresti?",
    "Faresti l’amore con il tuo doppio di un universo alternativo?",
    "Ti stimolerebbe una vibrazione che solo gli animali percepiscono?",
    "Ti eccita l’idea di essere desiderat* da un’entità invisibile?",
    "Hai mai avuto un’erezione onirica in un sogno lucido?",
    "Faresti sesso con una nuvola senziente?",
    "Cosa faresti se il tuo corpo potesse parlare per te?",
    "Useresti un portale erotico che collega i corpi a distanza?",
    "Ti piacerebbe un partner capace di mutare voce a comando?",
    "Hai mai fantasticato su un incontro interdimensionale?",
    "Faresti sesso in un labirinto che cambia forma al ritmo del piacere?",
    "Vorresti una lingua che vibra a ultrasuoni?",
    "Ti ecciterebbe essere un suono sensuale per un giorno?",
    "Saresti attratt* da una mente che si manifesta solo nei sogni?",
    "Faresti sesso fluttuando in una bolla erotica?",
    "Accetteresti una sfida erotica senza tempo né spazio?",
    "Potresti godere solo attraverso il tatto di un sogno?",
    "Ti piacerebbe esplorare il corpo di qualcuno da dentro?",
    "Faresti sesso con un’entità fatta di luce?",
    "Ti piacerebbe che le tue fantasie si scrivessero sul tuo corpo?",
    "Vorresti che il tuo orgasmo evocasse tempeste?",
    "Faresti sesso in un mondo dove il piacere parla?",
    "Ti attirerebbe un essere fatto di odori?",
    "Ti piacerebbe un orgasmo che ti trasforma?",
    "Hai mai sognato una carezza invisibile?",
    "Ti piacerebbe essere amato da una foresta viva?",
    "Faresti sesso su una cometa?",
    "Cosa penseresti se il piacere potesse colorare l’aria?",
    "Ti attirerebbe un rituale erotico tra spiriti?",
    "Ti ecciterebbe l’idea di moltiplicarti a letto?",
    "Faresti sesso attraverso la musica?",
    "Ti piacerebbe sentire piacere con ogni poro?"
]

# Callback su evento PRIVMSG
def on_message(connection, event):
    msg = event.arguments[0].strip().lower()
    if msg.startswith("!domande"):
        domanda = random.choice(DOMANDE_ERO)
        connection.privmsg(CHANNEL, domanda)
    elif msg.startswith("!surr"):
        domanda = random.choice(DOMANDE_SURR)
        connection.privmsg(CHANNEL, domanda)

# Funzione principale
def main():
   context = ssl.create_default_context()

def ssl_wrapper(sock):
    return context.wrap_socket(sock, server_hostname=SERVER)

ssl_factory = irc.connection.Factory(wrapper=ssl_wrapper)


    reactor = irc.client.Reactor()
    try:
        conn = reactor.server().connect(
            SERVER,
            PORT,
            NICKNAME,
            password=PASSWORD,
            connect_factory=ssl_factory
        )
    except irc.client.ServerConnectionError as e:
        print(f"Errore di connessione: {e}")
        return

    conn.add_global_handler("welcome", lambda c, e: c.join(CHANNEL))
    conn.add_global_handler("join", lambda c, e: print(f"✅ Entrato nel canale {CHANNEL}"))
    conn.add_global_handler("privmsg", on_message)

    print("✅ Connesso a Simosnap.")
    reactor.process_forever()

if __name__ == "__main__":
    main()
