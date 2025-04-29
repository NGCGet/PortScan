import socket
import sys


def scan(host, portas):
    try:
        for porta in portas:
            client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client.settimeout(0.05)
            code = client.connect_ex((host, int(porta)))

            if code == 0:
                print("{} - open".format(porta))
    except Exception as error:
        print(error)

if __name__ == "__main__":
    if len(sys.argv) >= 2:
        host = sys.argv[1]
        if len(sys.argv) >= 3:
            portas = sys.argv[2].split(",")
        else:
            portas = [21, 22, 23, 24, 25, 80, 135, 139, 433, 445, 8080, 8433, 3306]

        scan(host, portas)
    else:
        print("usage: python portscan.py google.com 22,23,80,443")