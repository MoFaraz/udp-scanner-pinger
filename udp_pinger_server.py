import random
from socket import *

# Create a UDP socket
# Notice the use of SOCK_DGRAM for UDP packets
serverSocket = socket(AF_INET, SOCK_DGRAM)
# Assign IP address and port number to socket
serverSocket.bind(('', 12000))
print("Started UDP server on port 12000")
while True:
    try:
        rand = random.randint(0, 10)
        message, address = serverSocket.recvfrom(1024)
        message = message.upper()
        print('Message {} is recived'.format(message))
        if rand < 4:
         continue
        serverSocket.sendto(message, address)
    except KeyboardInterrupt:
       print("good bye")
       break