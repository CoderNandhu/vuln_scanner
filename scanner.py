import socket
import requests
import nmap

target = input("Enter the target domain or IP: ")

# Port Scanner using socket
def scan_ports():
    print("\n[+] Scanning ports 1 to 100...")
    for port in range(1, 101):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket.setdefaulttimeout(0.5)
            result = sock.connect_ex((target, port))
            if result == 0:
                print(f"[OPEN] Port {port}")
            sock.close()
        except:
            pass

# Grab HTTP Headers
def grab_headers():
    print("\n[+] Fetching HTTP headers...")
    try:
        res = requests.get(f"http://{target}", timeout=3)
        for header, value in res.headers.items():
            print(f"{header}: {value}")
    except requests.ConnectionError:
        print("[!] No web server detected on port 80.")
    except Exception as e:
        print(f"Error: {e}")

# Banner Grabbing
def grab_banner(port):
    try:
        s = socket.socket()
        s.connect((target, port))
        s.settimeout(2)
        banner = s.recv(1024).decode().strip()
        print(f"[+] Banner on port {port}: {banner}")
        s.close()
    except:
        pass

# Nmap Scan
def nmap_scan():
    print("\n[+] Running Nmap scan (1-100)...")
    nm = nmap.PortScanner()
    nm.scan(target, '1-100')
    for host in nm.all_hosts():
        print(f"\nHost: {host} ({nm[host].state()})")
        for proto in nm[host].all_protocols():
            print(f"Protocol: {proto}")
            ports = nm[host][proto].keys()
            for port in sorted(ports):
                print(f"Port: {port} \tState: {nm[host][proto][port]['state']}")

# Run All
scan_ports()
grab_headers()
for p in [21, 22, 80, 443]:
    grab_banner(p)
nmap_scan()
