import irc.client
import irc.connection
import ssl
import random
import threading

SERVER = "irc.simosnap.org"
PORT = 6697
NICKNAME = "InutileOrgasmo"
PASSWORD = "Inutili2025Orgasmi"
CHANNEL = "#orgasmiinutili"

DOMANDE_EROTICHE = [
    "Qual è la tua fantasia più segreta?",
    "Hai mai fatto sesso in un luogo pubblico?",
    "Preferisci dominare o essere dominato?",
    "Ti piace il dirty talk?",
    "Hai mai avuto un sogno erotico ricorrente?",
    "Qual è stata la tua esperienza più eccitante?",
    "Ti piace sperimentare con nuovi giochi erotici?",
    "Hai mai fatto un threesome?",
    "Hai mai fatto sexting spinto?",
    "Cosa ti accende di più durante un incontro?",
    # ... continua fino a 40
]

DOMANDE_SURREALI = [
    "Hai mai fatto l'amore con un'ombra?",
    "Ti sei mai eccitato guardando una teiera?",
    "Cosa ti fa più effetto: un bacio o un'equazione?",
    "Se il piacere fosse un frutto, quale sarebbe?",
    "Hai mai sognato di sedurre una nuvola?",
    "Se potessi flirtare con un colore, quale sceglieresti?",
    "Ti ha mai baciato il vento in modo indecente?",
    "Hai mai provato attrazione per un'idea astratta?",
    "Hai mai fatto l’amore dentro un sogno di qualcun altro?",
    "Ti sei mai innamorato di un pensiero ricorrente?",
    # ... continua fino a 40
]

def on_welcome(connection, event):
    print("🔗 Connesso. Invio IDENTIFY a NickServ...")
    connection.privmsg("NickServ", f"IDENTIFY {PASSWORD}")

def on_notice(connection, event):
    sender = event.source or ""
    msg = event.arguments[0].lower()

    print(f"🔔 NOTICE da {sender}: {msg}")

    if "sei già identificato" in msg or "you are now identified" in msg:
        print(f"✅ Identificato! Entro in {CHANNEL}...")
        connection.join(CHANNEL)

def on_join(connection, event):
    print(f"👋 Entrato nel canale {CHANNEL}.")

def on_message(connection, event):
    msg = event.arguments[0].strip().lower()
    if msg == "!domande":
        domanda = random.choice(DOMANDE_EROTICHE)
        connection.privmsg(CHANNEL, f"🔞 {domanda}")
    elif msg == "!surr":
        domanda = random.choice(DOMANDE_SURREALI)
        connection.privmsg(CHANNEL, f"🌀 {domanda}")

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
            connect_factory=ssl_factory
        )
    except irc.client.ServerConnectionError as e:
        print(f"❌ Errore di connessione: {e}")
        return

    conn.add_global_handler("001", on_welcome)
    conn.add_global_handler("notice", on_notice)
    conn.add_global_handler("join", on_join)
    conn.add_global_handler("privmsg", on_message)

    print("🟢 In ascolto...")
    reactor.process_forever()

if __name__ == "__main__":
    main()
