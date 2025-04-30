import irc.client
import irc.connection
import ssl

def main():
    server = "irc.simosnap.org"
    port = 6697  # porta SSL
    nickname = "InutileBot"  # cambia se il nick è già usato
    realname = "InutileOrgasmo"
    channel = "#inutile"  # cambia con il canale dove vuoi entrare

    # Setup SSL connection factory
    ssl_factory = irc.connection.Factory(wrapper=ssl.wrap_socket)

    # Reactor setup
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

    # Aggiungi i tuoi handler qui (es. per on_connect, on_privmsg, ecc.)
    def on_connect(connection, event):
        print(f"Connected to {server}, joining {channel}")
        connection.join(channel)

    def on_disconnect(connection, event):
        print("Disconnected from server")

    conn.add_global_handler("welcome", on_connect)
    conn.add_global_handler("disconnect", on_disconnect)

    # Avvia il loop
    reactor.process_forever()
