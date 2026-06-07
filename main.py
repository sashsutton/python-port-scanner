import socket

from IPy import IP

# target = "192.168.1.0/24"
target1 = "192.0.0.2"


def check_ip(target):
    try:
        ip = IP(target)
        return target

    except ValueError:
        return socket.gethostbyname(target)


print(check_ip(target1))


def scan_port(ip_adress, port):
    try:
        sock = socket.socket()
        sock.settimeout(0.5)
        sock.connect((ip_adress, port))
        print(f"[+] Port {port} is open")
        sock.close()
    except:
        pass
