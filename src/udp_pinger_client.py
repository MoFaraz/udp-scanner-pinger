import socket
import time

def find_rtt(target, port):
    host = socket.gethostbyname(target)
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_addr = (host, port)
    udp_socket.settimeout(1)

    try:
        for i in range(1, 11):
            start = time.time()
            message = 'Ping #' + str(i) + " " + time.ctime(start)
            message1 = message.encode()
            try:
                print("Sent " + message)
                sent = udp_socket.sendto(message1, server_addr)
                data, server = udp_socket.recvfrom(4096)
                data = data.decode()
                print("Received " + data)
                end = time.time()
                elapsed = end - start
                print("RTT: " + str(elapsed) + " seconds\n")
            except socket.timeout:
                print("#" + str(i) + " Requested Time out\n")
            except socket.error:
                print("something went wrong")

    finally:
        udp_socket.close()