from socket import *
serverName = 'localhost'	# or 'hostname' 'IP address'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_DGRAM)

while True:
    message = input('Send sorted numbers: ')
    element = input('Send an element to server: ')
    clientSocket.sendto(message.encode(),(serverName, serverPort))
    clientSocket.sendto(element.encode(),(serverName, serverPort))
    modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
    a = modifiedMessage.decode()
    print(f"Yes there is a number {element} at index: {a}")
clientSocket.close()
  
    
