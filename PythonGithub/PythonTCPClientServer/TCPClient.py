# importing socket module
from socket import *
import sys

# identifying server that we want to connect to
serverName = "localhost"
serverPort = 12000

# Making socket, TCP connection because of SOCK_STREAM
clientSocket = socket(AF_INET, SOCK_STREAM)
message = ""

# Connecting to server identified by variables above
try:
    clientSocket.connect((serverName, serverPort))

    # input a message to encode into bytes and sending it to server
    while message != "bye":
        message = input("Enter a message: ")
        messageBytes = str.encode(message)  # converting message to bytes
        clientSocket.send(messageBytes)

        # Receives message from server, identifies where it came from and prints message, closes socket
        messageFromServerBytes = clientSocket.recv(1024)
        print(bytes.decode(messageFromServerBytes), "from", (serverName, serverPort))



except gaierror as err:
    print("No Host Found.")
    print(err)
    sys.exit()

except OSError as err:
    print("Something went wrong.")
    print(err)

clientSocket.close()
