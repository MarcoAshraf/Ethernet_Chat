import socket
import threading

server_ip = "169.254.244.176"


# AF_Inet for IPV4 and SOCK_STREAM for TCP/IP
c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# write the server IP and port number
ip = server_ip
port = 1997
# connect to the server
c.connect((ip, port))


def send_message():
    while 1:
        message = input("Enter something: \n")
        message = message.encode("utf-8")
        c.send(message)


def receive_message():
    while 1:
        try:
            message = (c.recv(1024)).decode("Utf-8")
            print(message)
        except:
            continue


receive_thread = threading.Thread(target=receive_message)
send_thread = threading.Thread(target=send_message)

receive_thread.start()
send_thread.start()

receive_thread.join()
send_thread.join()
