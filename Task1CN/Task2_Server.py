from socket import *
serverPort = 12000
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('',serverPort))
print("Server is ready to receive :) ")

while True:
    message, clientAddress = serverSocket.recvfrom(2048)
    element, clientAddress = serverSocket.recvfrom(2048)
    text = message.decode()
    shift = element.decode()
    #print(modifiedMessage)
    #print(elmnt)
    def encrypt(text, shift):
        result = ""
         # traverse text
        for i in range(len(text)):
            char = text[i]
            
            if (char.isupper()):
                result += chr((ord(char) + shift - 65) % 26 + 65)
            else:
                result += chr((ord(char) + shift - 97) % 26 + 97)
        return result
    x = encrypt(text,int(shift))
    serverSocket.sendto(x.encode(), clientAddress)

