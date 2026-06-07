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
