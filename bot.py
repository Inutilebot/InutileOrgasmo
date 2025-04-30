import irc.client
import irc.connection
import ssl

def main():
    server = "irc.simosnap.org"
    port = 6697
    nickname = "InutileBot"        # cambia se necessario
    realname = "InutileOrgasmo"
    channel = "#inutile"           # cambia col canale che vuoi usare
    nickserv_password = "Inutili2025Orgasmi"  # ← sostituisci se usi NickServ, oppure lascia ""

    ssl_factory = irc.connection.Factory(wrapper=ssl.wrap_socket)

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
        print(f"Connection failed: {e}")
        return

    def on_connect(connection, event):
        print(f"Connected to {server}")
        # Autenticazione con NickServ, se serve
        if nickserv_password:
            connection.privmsg("NickServ", f"IDENTIFY {nickserv_password}")
        connection.join(channel)

    def on_join(connection, event):
        if event.source.nick == nickname:
            print(f"Joined channel {channel}")
            connection.privmsg(channel, "Ciao a tutti, sono tornato.")

    def on_disconnect(connection, event):
        print("Disconnected from server.")

    conn.add_global_handler("welcome", on_connect)
    conn.add_global_handler("join", on_join)
    conn.add_global_handler("disconnect", on_disconnect)

    reactor.process_forever()
