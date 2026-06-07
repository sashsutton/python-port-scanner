import socket
import threading

from IPy import IP

# 127.0.0.1

target1 = "127.0.0.1"


def check_ip(target):
    try:
        ip = IP(target)
        return target

    except ValueError:
        return socket.gethostbyname(target)


def scan_port(ip_adress, port):
    try:
        sock = socket.socket()
        sock.settimeout(0.5)
        sock.connect((ip_adress, port))
        print(f"[+] Port {port} is open")
        sock.close()
    except:
        pass


def scan(target):
    converted_ip = check_ip(target)
    print("\n + [# Scanning Target] " + str(target))

    threads = [
        threading.Thread(target=scan_port, args=(converted_ip, i))
        for i in range(1, 65536)
    ]

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

    return threads


if __name__ == "__main__":
    scan(target1)
