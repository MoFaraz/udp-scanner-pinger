from udp_scanner import Udp_Socket
import subprocess

if __name__ == "__main__":
    try: 
        while True:
            user_input = input("\n[1] udp-port-scanner  [2] udp-pinger\n")
        
            if user_input == '1':
                Udp_Socket('localhost')
            elif user_input == '2':
                exec(open('udp_pinger_client.py').read())                
            elif user_input.lower() == 'q':
                print("Exiting program.")
                break
    except KeyboardInterrupt:
        print('good bye')
    
   