import socket


ip_address = None
start_range = None
end_range = None
common_ports = [20,21,22,23,25,53,80,110,143,443,3306,3389,5500,8080]


while True:
    try:
        domain_or_ip = int(input("enter 1 for host name or 2 ip address: "))
        if domain_or_ip == 1:
            target_domain_name= input("enter the domain name: ")
            try:
                ip_address = socket.gethostbyname(target_domain_name)
                print("resolved ip address", ip_address)
            except socket.gaierror:
                print("could not resolve, ip address")
            break
    
        elif domain_or_ip == 2:
            ip_address = input("enter the ip address: ")
            try:
                socket.inet_pton(socket.AF_INET, ip_address)
                print(ip_address)
            except OSError:
                print("not a valid ip address")
            break

        else:
            print("Enter a valid number")
    except ValueError:
        print("choose between 1 and 2")

while True:
    try:
        start_range = int(input("Enter where the port scanning should start from: "))
        end_range = int(input("Enter where the port scanning should end: "))
        if start_range >= 1 and end_range <= 65535:
            print(f"scanning ports {start_range} to {end_range}......")
            break
        else:
            ("invalid range, enter a correct range from 1 to 65535")
    except ValueError:
        print("enter a value")

ports_to_scan = []
for port in common_ports:
    if start_range <= port <= end_range:
        ports_to_scan.append(port)
print(ports_to_scan)

for p in ports_to_scan:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(3)
    result = sock.connect_ex((ip_address,p))

    if result == 0:
        print(f"port {p} is open")
    else:
        print(f"port{p} is closed")
    sock.close()