import socket
import time

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_addr = ('127.0.0.1', 12000)
sock.settimeout(1)

try:
    for i in range(1, 11):
        start = time.time()
        message = 'Ping #' + str(i) + " " + time.ctime(start)
        message1 = message.encode()
        try:
            sent = sock.sendto(message1, server_addr)
            print("Sent " + message)
            data, server = sock.recvfrom(4096)
            data = data.decode()
            print("Received " + data)
            end = time.time();
            elapsed = end - start
            print("RTT: " + str(elapsed) + " seconds\n")
        except socket.timeout:
            print("#" + str(i) + " Requested Time out\n")

finally:
    print("closing socket")
    sock.close()