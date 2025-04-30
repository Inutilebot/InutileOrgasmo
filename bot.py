import socket
import random
import time
import os

server = "irc.simosnap.com"
port = int(os.getenv("PORT", 6667))  # Usa la porta di Render, altrimenti la porta di default (6667)
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

irc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
irc.connect((server, port))
irc.send(f"PASS {password}\r\n".encode())
irc.send(f"NICK {nickname}\r\n".encode())
irc.send(f"USER {nickname} 0 * :{nickname}\r\n".encode())
irc.send(f"JOIN {channel}\r\n".encode())

def send_message(msg):
    irc.send(f"PRIVMSG {channel} :{msg}\r\n".encode())

while True:
    try:
        data = irc.recv(2048).decode(errors="ignore")
        print(data)

        if data.startswith("PING"):
            irc.send(f"PONG {data.split()[1]}\r\n".encode())

        if "!domande" in data:
            domanda = random.choice(domande_normali)
            send_message(f"Domanda erotica: {domanda}")

        if "!stocazzo" in data:
            domanda = random.choice(domande_surreali)
            send_message(f"Domanda surreale: {domanda}")

        time.sleep(1)

    except KeyboardInterrupt:
        break
