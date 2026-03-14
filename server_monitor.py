import platform
import psutil

def get_server_info():
    print("=== 服务器基础信息 ===")
    print(f"系统版本：{platform.system()} {platform.release()}")
    print(f"主机名：{platform.node()}")
    print(f"CPU 核心数：{psutil.cpu_count()}")
    print(f"内存使用率：{psutil.virtual_memory().percent}%")
    print(f"磁盘使用率：{psutil.disk_usage('/').percent}%")

if __name__ == "__main__":
    get_server_info()
    print("\n脚本用途：用于监控服务器硬件资源，辅助日常运维巡检")
