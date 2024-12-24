import threading

class netbot:
    def __init__(self, id, is_start, ip_address):
        self.id = id
        self.is_start = is_start
        self.ip_address = ip_address


class Server:
    def __init__(self):
        self.socketfd = -1

        self.attacking = False
        self.attack = "None"

        self.target_ip = "None"
        self.target_port = 0

        self.netbots = []
        self.tListener = threading.Thread()

    def get_server_fd(self):
        return self.socketfd
    
    def set_server_fd(self, socketfd):
        self.socketfd = socketfd

    def server_status():
        
    def setup_target_parameters():
        
    def start_attack():
        
    def close_connected_sockets():
    
    def list_bots():
        
    def setup_attack_type():
        
    def threaded():
    
    def connection_listener():    
    
