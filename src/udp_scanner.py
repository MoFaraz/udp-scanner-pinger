import pyfiglet
import socket
import sys
import time

def Udp_Socket(target):
    host = socket.gethostbyname(target)
    for port in range(1, 1024):
        udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        udp_socket.settimeout(0.001)
        result = udp_socket.connect_ex((host, port))
        try:
            if result == 0:
                print(f"port {port} is open and it's service is: {socket.getservbyport(port, "udp")}")
            elif result != 0:
                print(f"port {port} is closed")
        except socket.error:
            continue
            #print(f"port {port} is open and it's service is: Unkown")

def Tcp_Socket(host):
    for port in range(1, 1024):
        tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        tcp_socket.settimeout(0.001)
        result = tcp_socket.connect_ex((host, port))
        try:
            if result == 0:
                print(f"port {port} is open and it's service is: {socket.getservbyport(port, "tcp")}")
            else:
                #print("port is closed")
                continue
        except socket.error:
            continue

