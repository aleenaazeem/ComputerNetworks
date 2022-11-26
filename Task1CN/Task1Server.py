from socket import *
serverPort = 12000
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('',serverPort))
print("Server is ready to receive :) ")

while (1):
    message, clientAddress = serverSocket.recvfrom(2048)
    element, clientAddress = serverSocket.recvfrom(2048)
    modifiedMessage = message.decode()
    elmnt = element.decode()
    print(modifiedMessage)
    print(elmnt)
    List1 = modifiedMessage.split(',')
    for i in range (0,len(List1)-1):
        if List1[i] == elmnt:
            index = str(i)
            serverSocket.sendto(index.encode(), clientAddress)

    
