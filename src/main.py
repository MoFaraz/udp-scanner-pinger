from udp_scanner import Udp_Socket, Tcp_Socket
from udp_pinger_client import find_rtt
from udp_pinger_server import start_server
import threading
import sys
import pyfiglet

def print_pyfiglet(context, myfont):
    print(pyfiglet.figlet_format(context, font=myfont))

if __name__ == "__main__":
    print_pyfiglet("UDP_SCANNER_PINGER", "digital")
    print_pyfiglet("FARAZMAND___MORADI", "digital")
    server_thread = threading.Thread(target=start_server, args=('localhost',12000))
    server_thread.daemon = True
    server_thread.start()
    try: 
        while True:
            user_input = input("\n[1] udp-port-scanner  [2] udp-pinger  [q] exit\n")
            if user_input == '1':
                Udp_Socket('localhost')
                #Tcp_Socket('localhost')
            elif user_input == '2':
                find_rtt('localhost', 12000)
            elif user_input == 'q':
                print("good bye") 
                sys.exit()
            else:
                print("Please Input Numer [1] or [2]")
    except KeyboardInterrupt:
        print('good bye')
        sys.exit()
   