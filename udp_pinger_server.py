import random
import socket

def start_server(target, port):
    host = socket.gethostbyname(target)
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udp_socket.bind((host, port))
    print("Started UDP server on port 12000")
    while True:
        rand = random.randint(0, 10)
        message, address = udp_socket.recvfrom(1024)
        message = message.upper()
        print(f'Message {message} is recived')
        if rand < 4:
            continue
        udp_socket.sendto(message, address)
        