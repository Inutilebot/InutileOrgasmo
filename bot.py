import irc.client
import irc.connection
import random

SERVER = "irc.simosnap.org"
PORT = 6667
NICKNAME = "InutileOrgasmo"
PASSWORD = "Inutili2025Orgasmi"
CHANNEL = "#orgasmiinutili"

DOMANDE_EROTICHE = [
    "Qual è la tua fantasia più segreta?",
    "Hai mai fatto sesso in un luogo pubblico?",
    "Preferisci dominare o essere dominato?",
    "Ti piace il dirty talk?",
    "Hai mai avuto un sogno erotico ricorrente?",
    # ... altre fino a 40
]

DOMANDE_SURREALI = [
    "Hai mai fatto l'amore con un'ombra?",
    "Ti sei mai eccitato guardando una teiera?",
    "Cosa ti fa più effetto: un bacio o un'equazione?",
    "Se il piacere fosse un frutto, quale sarebbe?",
    "Hai mai sognato di sedurre una nuvola?",
    # ... altre fino a 40
]

def on_welcome(connection, event):
    print("✅ Autenticato con SASL, ora entro nel canale...")
    connection.join(CHANNEL)

def on_join(connection, event):
    print(f"👋 Entrato in {CHANNEL}")

def on_privmsg(connection, event):
    msg = event.arguments[0].strip().lower()
    if msg == "!domande":
        connection.privmsg(CHANNEL, f"🔞 {random.choice(DOMANDE_EROTICHE)}")
    elif msg == "!surr":
        connection.privmsg(CHANNEL, f"🌀 {random.choice(DOMANDE_SURREALI)}")

def main():
    reactor = irc.client.Reactor()

    factory = irc.connection.Factory()
    try:
        conn = reactor.server().connect(
            SERVER,
            PORT,
            NICKNAME,
            password=PASSWORD,
            connect_factory=factory,
            username=NICKNAME,
            ircname=NICKNAME
        )
    except irc.client.ServerConnectionError as e:
        print(f"❌ Errore di connessione: {e}")
        return

    conn.cap("REQ", "sasl")
    conn.cap("END")
    conn.add_global_handler("welcome", on_welcome)
    conn.add_global_handler("join", on_join)
    conn.add_global_handler("privmsg", on_privmsg)

    print("🟢 Bot in ascolto...")
    reactor.process_forever()

if __name__ == "__main__":
    main()
