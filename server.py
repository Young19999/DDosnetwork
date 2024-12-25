import threading
import socket

class netbot:
    def __init__(self, id, is_start, ip_address):
        self.id = id
        self.is_start = is_start
        self.ip_address = ip_address


class Server:
    def __init__(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        self.attacking = False
        self.attack = "None"

        self.target_ip = "None"
        self.target_port = 0

        self.netbots = []
        self.threads = []
        self.tListener = threading.Thread()

    def server_status():
        
    def setup_target_parameters(self):
        pass
        
    def start_attack(self):
        pass
        
    def close_connected_sockets(self):
        pass
    
    def list_bots(self):
        pass
        
    def setup_attack_type(self):
        pass
        
    def threaded(self):
        pass
    
    def connection_listener(self):  
        pass  
    
