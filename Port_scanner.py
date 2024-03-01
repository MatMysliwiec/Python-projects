import socket


def port_scanner(target_ip, start_port, end_port):
    open_ports = []

    for port in range(start_port, end_port):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)

        try:
            sock.connect((target_ip, port))
            open_ports.append(port)
            print(f"Port {port} is open")
        except (socket.timeout, socket.error):
            pass
        finally:
            sock.close()
    return open_ports


if __name__ == "__main__":
    target_ip = input("Enter target IP address: ")
    start_port = int(input("Enter starting port: "))
    end_port = int(input("Enter end port: "))

    open_ports = port_scanner(target_ip, start_port, end_port)

    if open_ports:
        print(f"Open ports on {target_ip}: {', '.join(map(str, open_ports))}")
    else:
        print("No open ports found.")
