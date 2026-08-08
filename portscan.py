import socket
import sys


def scan(host, portas):
    for porta in portas:
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
                client.settimeout(0.5)
                code = client.connect_ex((host, int(porta)))

                if code == 0:
                    print(f"Porta {porta} - aberta")
        except socket.gaierror:
            print(f"Erro: Não foi possível resolver o host '{host}'.")
            break
        except Exception as error:
            print(f"Erro ao verificar porta {porta}: {error}")


if __name__ == "__main__":
    if len(sys.argv) >= 2:
        host = sys.argv[1]

        if len(sys.argv) >= 3:
            portas = sys.argv[2].split(",")
        else:
            portas = [21, 22, 23, 25, 80, 135, 139, 443, 445, 3306, 8080, 8443]

        scan(host, portas)
    else:
        print("Uso correto: python portscan.py google.com 22,23,80,443")
