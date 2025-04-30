import irc.client
import irc.connection
import ssl
import random

# Lista di 40 domande erotiche assurde (!domande)
domande_erotiche = [
    "Hai mai fatto l’amore con una lampada accesa solo sul comodino?",
    "Quante volte ti sei spogliato pensando a una fotocopiatrice?",
    "Ti sei mai eccitato leggendo il manuale del microonde?",
    "Hai mai sognato un'orgia con i personaggi dei cartoni animati?",
    "Preferisci leccare un gelato o...?",
    "Hai mai chiesto a Siri di dirti cose sporche?",
    "Hai mai provato a sedurre una pianta da appartamento?",
    "Ti sei mai messo del burro sul corpo solo per sentire l’emozione?",
    "Hai mai fatto un sogno erotico con una stampante?",
    "Hai mai sentito attrazione per un semaforo?",
    "Hai mai spogliato mentalmente il tuo fruttivendolo?",
    "Hai mai fatto un massaggio hot a una sedia da ufficio?",
    "Hai mai pensato di baciare una statua?",
    "Hai mai guardato un documentario sugli animali... per eccitarti?",
    "Hai mai provato il brivido di togliere le calze lentamente davanti allo specchio?",
    "Hai mai ballato nudo ascoltando sigle dei cartoni?",
    "Ti sei mai messo del miele sul corpo senza motivo?",
    "Hai mai toccato la lavatrice durante la centrifuga... con passione?",
    "Hai mai sussurrato cose sporche al tuo aspirapolvere?",
    "Hai mai avuto pensieri sporchi su un oggetto da cucina?",
    "Hai mai dato un nome erotico al tuo cuscino?",
    "Hai mai fatto l’amore con gli occhi a una tazza di caffè?",
    "Ti sei mai spogliato solo per te stesso alle 3 di notte?",
    "Hai mai pensato a un bidet in modo sconveniente?",
    "Hai mai sognato una doccia sensuale con le tende chiuse?",
    "Ti eccita il rumore del frullatore?",
    "Hai mai annusato un libro vecchio e provato piacere?",
    "Hai mai accarezzato il volante come se fosse una persona?",
    "Hai mai detto “ti amo” al tuo phon?",
    "Hai mai trovato sexy un foglio di alluminio?",
    "Hai mai avuto una fantasia con la carta igienica a due veli?",
    "Hai mai desiderato sedurre il tuo specchio?",
    "Hai mai fatto un selfie nudo solo per guardarlo subito dopo?",
    "Hai mai baciato il telecomando?",
    "Hai mai danzato nudo con la finestra aperta?",
    "Hai mai parlato sporco a te stesso in uno specchio?",
    "Hai mai messo vestiti sexy solo per buttare la spazzatura?",
    "Hai mai sognato di limonare con la lavastoviglie?",
    "Hai mai trovato erotico il suono del microonde?"
]

# Lista di 40 domande erotiche surreali (!stocazzo)
domande_surrealiste = [
    "Se un pene cade in un bosco e nessuno lo sente, fa rumore?",
    "L’universo si espande o si eccita?",
    "I capezzoli hanno una coscienza propria?",
    "Cosa sogna un dildo quando dorme?",
    "È possibile avere un’erezione quantistica?",
    "L’amore platonico tra due vibratori è reale?",
    "Una vagina può avere nostalgia?",
    "Se il sesso fosse un frutto, sarebbe un’ananas o un fico?",
    "Esistono orgasmi paralleli in dimensioni alternative?",
    "Può uno starnuto essere erotico?",
    "Il big bang era un’eiaculazione cosmica?",
    "Cosa succede se due ombre fanno sesso?",
    "Un orgasmo può viaggiare nel tempo?",
    "Il desiderio ha una massa misurabile?",
    "Se ti masturbi in sogno, il tuo corpo gode davvero?",
    "Può un pensiero spogliarsi?",
    "Il profumo del desiderio esiste o lo immaginiamo?",
    "Un sospetto di attrazione è già tradimento mentale?",
    "Può un sospiro ingravidare un’idea?",
    "L’orgasmo è un parente del Big Crunch?",
    "Esistono gatti che si eccitano filosoficamente?",
    "Il pudore è un virus o un'invenzione?",
    "L'eiaculazione è una fuga o un ritorno?",
    "Può un'idea avere un feticismo?",
    "Il piacere ha una frequenza radio?",
    "Un sogno erotico può rimanerti incinta l'anima?",
    "Gli specchi si eccitano vedendoci nudi?",
    "È immorale eccitarsi per un’equazione?",
    "Un bacio può attraversare le pareti?",
    "Un orgasmo può essere silenzioso e cosmico?",
    "Se Dio fa sesso, è blasfemia?",
    "L’amore può essere quantico e particellare insieme?",
    "Se ti masturbi in una simulazione, è reale?",
    "Il desiderio è una funzione d’onda?",
    "Può un'erezione essere platonica?",
    "Gli orgasmi si reincarnano?",
    "Cosa prova un pene quando è solo?",
    "L’eiaculazione è un’opinione universale?",
    "Può l’universo provare piacere quando lo guardi?"
]

# Configurazione IRC
server = "irc.simosnap.org"
port = 6697
nickname = "InutileOrgasmo"
realname = "Inutile Orgasmo"
channel = "#orgasmiinutili"
nickserv_password = "Inutili2025Orgasmi"

def main():
ssl_factory = irc.connection.Factory(wrapper=ssl.create_default_context().wrap_socket)
    reactor = irc.client.Reactor()

    try:
        conn = reactor.server().connect(
            server,
            port,
            nickname,
            realname=realname,
            connect_factory=ssl_factory
        )
    except irc.client.ServerConnectionError as e:
        print(f"Errore di connessione: {e}")
        return

    def on_connect(connection, event):
        print("✅ Connesso a Simosnap.")
        if nickserv_password:
            connection.privmsg("NickServ", f"IDENTIFY {nickserv_password}")
        connection.join(channel)

    def on_join(connection, event):
        if event.source.nick == nickname:
            print(f"✅ Entrato nel canale {channel}")
            connection.privmsg(channel, "Eccomi, sono l’orgasmo inutile.")

    def on_pubmsg(connection, event):
        messaggio = event.arguments[0].strip().lower()
        if messaggio == "!domande":
            domanda = random.choice(domande_erotiche)
            connection.privmsg(channel, f"Inutile domanda erotica: {domanda}")
        elif messaggio == "!stocazzo":
            domanda = random.choice(domande_surrealiste)
            connection.privmsg(channel, f"Inutile domanda surreale: {domanda}")

    def on_disconnect(connection, event):
        print("❌ Disconnesso.")

    conn.add_global_handler("welcome", on_connect)
    conn.add_global_handler("join", on_join)
    conn.add_global_handler("pubmsg", on_pubmsg)
    conn.add_global_handler("disconnect", on_disconnect)

    reactor.process_forever()

if __name__ == "__main__":
    main()
