from scanner.core import scan_ports
from scanner.utils import save_to_csv

def main():
    target = input("Enter target IP: ")
    ports = range(20, 1025)

    print(f"Scanning {target}...")
    results = scan_ports(target, ports)

    for port, status in results:
        print(f"Port {port}: {status}")

    save_to_csv(target, results)
    print("Results saved to CSV.")

if __name__ == "__main__":
    main()
