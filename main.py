from udp_scanner import Udp_Socket, Tcp_Socket
from udp_pinger_client import find_rtt
from udp_pinger_server import start_server
import threading


if __name__ == "__main__":
    try: 
        while True:
            user_input = input("\n[1] udp-port-scanner  [2] udp-pinger\n")
            if user_input == '1':
                Udp_Socket('localhost')
                #Tcp_Socket('localhost')
            elif user_input == '2':
                server_thread = threading.Thread(target=start_server, args=('localhost',12000))
                server_thread.start()
                find_rtt('localhost', 12000)
            else:
                print("Please Input Numer [1] or [2]")
    except KeyboardInterrupt:
        print('good bye')
    
   