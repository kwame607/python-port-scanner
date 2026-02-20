#!/usr/bin/env python
import time
import socket
from pyfiglet import Figlet

f = Figlet(font='graffiti')
text = "CRAZY's Port Scanner"
newText = f.renderText(text)
print(f"\033[1;31m{newText}\033[0m")
print("\t \t \033[1;32m********************************\033[0m") 
print("\t \t \033[1;32m   		Coded by Crazy\033[0m")
print("\t \t \033[1;32m**********************************\033[0m")  
print("")

ip_address = None
start_range = None
end_range = None

while True:
	try:
		choice = int(input("\033[1;34m [?] Enter '1' to scan by host name or '2' to scan by IP address  : \033[0m"))
		
		if choice == 1:
			host_name =input("\033[1;34m [?] Enter the hostname/domain name: \033[0m")
			try:
				ip_address = socket.gethostbyname(host_name)
				print(f"\033[1;36m [*] Resolving... {host_name} → {ip_address}\033[0m")
				print(f"\033[34m [*] Checking if {ip_address} is up.....\033[0m")
			except socket.gaierror:
				print(f"\033[1;34m [!] Could not resolve {host_name}. Try again\033[0m")
			break
		
		elif choice == 2:
			ip_address = input("\033[1;34m [?] Enter the IP address: \033[0m")
			try:
				socket.inet_pton(socket.AF_INET, ip_address)
				print(f"\033[1;36m[-] Target set → {ip_address}\033[0m")
				print(f"\033[34m [*] Checking if {ip_address} is up..... \033[0m")
			except OSError:
				print(f"\033[1;34m [!] Invalid IP address. Try again. \033[0m")
			break
		else:
			print("\033[1;31m [!] Invalid Choice. Select '1' and '2'\033[0m")
	except ValueError:
		print("\033[1;31m [!] Invalid input. Enter a number; '1' or '2' \033[0m")


while True:
	try:
		start_range = int(input("\033[1;34m [?] Enter starting port : \033[0m "))
		end_range = int(input("\033[1;34m [?] Enter ending port : \033[0m"))
		if 1 <= start_range <= 65535 and 1<= end_range <= 65535 and start_range <= end_range:
			break
		else:
			print("\033[31m [!] Invalid range. Must be between 1-65535 inclusion \033[0m")
	except ValueError:
		print("\033[31m [!]Invalid input. Enter numbers only \033[0m")
		
tcp_protocols = input("\033[1;34m [-] Scan Mode → Type 'YES' for full range, or 'NO' for common ports only: \033[0m")

if tcp_protocols.lower() == "no":
	common_ports = [20,21,22,23,25,53,80,110,143,443,3306,3389,5500,8080]
	ports_to_scan = []
	print(f"\033[36m  [*] Scanning common ports between {start_range} and {end_range}......\033[0m ")

	for port in common_ports:
		if start_range<= port <=end_range:
			ports_to_scan.append(port)
	for p in ports_to_scan:
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		sock.settimeout(1)
		result = sock.connect_ex((ip_address,p))
		
		if result == 0:
			print(f"\033[1;32m  [+] port {p} is open \033[0m ")
		else:
			print(f"\033[1;31m  [-] port {p} is close \033[0m ")
		sock.close()

elif tcp_protocols.lower() == "yes":
	print(f"\033[1;34m [-] Scanning all ports between {start_range} and {end_range}...\033[0m")
	for port in range(start_range,end_range + 1):
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		sock.settimeout(0.1)
		result = sock.connect_ex((ip_address,port))

		if result == 0:
			print(f"\033[1;32m  [+] port {port} is open \033[0m ")
		sock.close()
else:
	print("\033[1;31m [!] Invalid choice. Please enter YES or NO.\033[0m")

print("\n")
bye = "\t \033[1;32mTHANK YOU FOR USING OUR SERVICE\033[0m"
for i in bye:
	print( i ,end ="", flush=True)
	time.sleep(0.1)
