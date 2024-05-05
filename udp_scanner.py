import pyfiglet
import socket
import sys
import time

def Udp_Socket(target):
    host = socket.gethostbyname(target)
    for port in range(1, 65535):
        try:
            udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            udp_socket.bind((host, port))
        except:
            try:
                print("port {} is open and it's service is: {}".format(port, socket.getservbyport(port, "udp")))
            except socket.error:
                print("port {} is open and it's service is: {}".format(port,"Unknown"))