import socket

def scan_ports(target, ports, timeout=0.5):
    results = []

    for port in ports:
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.settimeout(timeout)
                result = s.connect_ex((target, port))
                status = "Open" if result == 0 else "Closed"
                results.append((port, status))
        except Exception as e:
            results.append((port, f"Error: {e}"))

    return results
