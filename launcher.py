import subprocess
import time

def launch_netbot(instance_count: int):
    # 启动指定数量的 netbot 实例
    for i in range(instance_count):
        print(f"Launching netbot instance {i+1}...")
        try:
            # 启动 netbot.py 的新子进程
            subprocess.Popen(['python3', 'netbot.py'])
            time.sleep(1)  # 可以适当调整间隔时间，防止过快启动
        except Exception as e:
            print(f"Error launching netbot instance {i+1}: {e}")

if __name__ == "__main__":
    # 启动 5 个 netbot 实例（根据需求调整数量）
    launch_netbot(5)
