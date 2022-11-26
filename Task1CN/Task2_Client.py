from socket import *
serverName = 'localhost'	# or 'hostname' 'IP address'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_DGRAM)

while True:
    message = input('Write your text: ')
    element = input('Shift: ')
    clientSocket.sendto(message.encode(),(serverName, serverPort))
    clientSocket.sendto(element.encode(),(serverName, serverPort))
    modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
    a = modifiedMessage.decode()
    print(f"The new text given is: {a}")
clientSocket.close()
  
    
 
