import socket
server  = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("localhost",9995))
server.listen()

client , addr = server.accept()

exit=False

while not exit:
    msg = client.recv(1024).decode('utf-8')
    if msg == "quit":
        exit =True
    else:
        print(msg)
    massage= input("Massage : ")
    client.send(massage.encode('utf-8'))

client.close()
server.close()
