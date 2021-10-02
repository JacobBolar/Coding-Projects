# Importing socket module
from socket import *

# setting server name and port
serverName = "localhost"
serverPort = 12000

# creating server socket, SOCK_STREAM identifies socket as TCP and attaches the server socket to the server.
# variables initialized above
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind((serverName, serverPort))

# While loop to keep server on
while True:

    # Opens the connection for a client to talk to.
    serverSocket.listen(1)
    print("Server is ready to recieve")

    # accepts a connection to the server socket
    connectionSocket, clientAddress = serverSocket.accept()

    # Receiving message from client and prints the message from the client address
    messageFromClientBytes = connectionSocket.recv(1024)
    while messageFromClientBytes.decode() != "bye":
        print(messageFromClientBytes, "from", clientAddress)

        # takes the message and makes it all upper case and sends the upper-cased message back to client
        messageToClientBytes = messageFromClientBytes.upper()
        connectionSocket.send(messageToClientBytes)
        messageFromClientBytes = connectionSocket.recv(1024)
    else:
        connectionSocket.close()
