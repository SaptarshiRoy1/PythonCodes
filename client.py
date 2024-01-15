import socket
client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(("localhost",9995))

exit =False

while not exit:
    massage = input("Massage : ")
    client.send(massage.encode("utf-8"))


    msg = client.recv(1024).decode('utf-8')
    if msg == "quit":
        exit = True
    else:
        print(msg)


client.close()