import threading
import socket

clients = list()


def broadcast(message):
    for client in clients:
        print(f"client.send({message}.encode('utf-8'))")
        client.send(message.encode("Utf-8"))


def receive():
    while 1:
        try:
            for client in clients:
                message = client.recv(1024)
                message = message.decode("Utf-8")
                broadcast(message)
        except:
            continue


def accept():
    # AF_INET = IPV4, SOCK_STREAM = TCP
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.settimeout(1)
    # address of the server
    ip = "10.202.25.89"
    # Server port greater than 1223
    port = 1997
    # bind ip, port
    server.bind((ip, port))
    # max number of connections to this server
    server.listen(4)
    while 1:
        try:
            print("acc\n")
            # wait for a client to connect
            client, address = server.accept()
            print(f"one device is connected with address {address}")
            clients.append(client)

        except:
            continue


receive_thread = threading.Thread(target=receive)
accept_thread = threading.Thread(target=accept)

receive_thread.start()
accept_thread.start()

receive_thread.join()
accept_thread.join()



