import socket
import random
import time
import ssl  # Importa la libreria per SSL

server = "irc.simosnap.com"
port = 6697  # Cambia la porta a 6697 per supportare SSL
nickname = "inutileorgasmo"
password = "Inutili2025Orgasmi"
channel = "#orgasmiinutili"

domande_normali = [
    "Qual è la tua posizione preferita?",
    "Hai mai fatto sesso in un luogo pubblico?",
    "Ti piace usare giocattoli erotici?",
    "Hai mai avuto un sogno erotico imbarazzante?",
    "Ti sei mai eccitato/a durante una riunione?",
] * 8

domande_surreali = [
    "Se potessi fare sesso con un'entità cosmica, quale sarebbe?",
    "Ti eccita l'idea di accarezzare un buco nero?",
    "Hai mai sognato di fare l'amore con un pensiero?",
    "Preferiresti un'orgia con gatti parlanti o con statue animate?",
    "Ti sei mai eccitato guardando un semaforo cambiare colore?",
] * 8

# Crea la connessione socket
irc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Aggiungi supporto SSL alla connessione
irc = ssl.wrap_socket(irc)

# Connessione al server IRC con la porta 6697 (SSL)
irc.connect((server, port))
irc.send(f"PASS {password}\r\n".encode())
irc.send(f"NICK {nickname}\r\n".encode())
irc.send(f"USER {nickname} 0 * :{nickname}\r\n".encode())
irc.send(f"JOIN {channel}\r\n".encode())

def send_message(msg):
    """Funzione per inviare un messaggio nel canale IRC"""
    irc.send(f"PRIVMSG {channel} :{msg}\r\n".encode())

while True:
    try:
        # Ricevi i dati dal server IRC
        data = irc.recv(2048).decode(errors="ignore")
        print(data)

        # Rispondi al PING con un PONG per mantenere la connessione attiva
        if data.startswith("PING"):
            irc.send(f"PONG {data.split()[1]}\r\n".encode())

        # Rispondi ai comandi !domande e !stocazzo con le domande
        if "!domande" in data:
            domanda = random.choice(domande_normali)
            send_message(f"Domanda erotica: {domanda}")

        if "!stocazzo" in data:
            domanda = random.choice(domande_surreali)
            send_message(f"Domanda surreale: {domanda}")

        # Aggiungi una piccola pausa per evitare sovraccarico
        time.sleep(1)

    except KeyboardInterrupt:
        break