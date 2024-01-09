import socket
from termcolor import colored

COMMON_PORTS = {
    21: "FTP",
    22: "SSH",
    23: "Telnet",
    25: "SMTP",
    53: "DNS",
    80: "HTTP",
    110: "POP3",
    135: "RPC",
    139: "NetBIOS",
    143: "IMAP",
    443: "HTTPS",
    445: "SMB",
    1433: "MSSQL",
    3306: "MySQL",
    3389: "RDP",
    5900: "VNC"
}

def check_port(host, port):
    try:
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.settimeout(1) # timeout to prevent the connection from hanging indefinitely
        result = client.connect_ex((host, port))
        if result == 0: # if connection is successful
            if port in COMMON_PORTS: # check if the port corresponds to a common service
                service = COMMON_PORTS[port]
                print(colored(f"[+] Port {port} ({service}): Open", "green"))
            else:
                print(colored(f"[+] Port {port}: Open", "green"))
        client.close()

    except KeyboardInterrupt:
        exit()

    except socket.gaierror:
        print("Host name could not be resolved.")
        exit()

    except socket.error:
        pass

target = input("Enter IP address of the host: ")
min_port = int(input("Enter minimum port number: "))
max_port = int(input("Enter maximum port number: "))

for port in range(min_port, max_port+1):
    check_port(target, port)
