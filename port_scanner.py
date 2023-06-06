import socket

def scan_port(target_host, target_port):
	try:
		# Create a socket object
		with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
			# Set timeout for the connection attempt
			sock.settimeout(2)
			
			# Attempt to connect to the target host and port
			result = sock.connect_ex((target_host, target_port))
			
			# Check if the port is open
			if result == 0:
				return True
			
	except socket.error:
		return False

def port_scan(target_host, target_ports):
	open_ports = []
	
	for port in target_ports:
		if scan_port(target_host, port):
			open_ports.append(port)
	
	return open_ports

def print_open_ports(open_ports):
	if len(open_ports) > 0:
		print("Open ports:")
		for port in open_ports:
			print(f"- Port {port} is open")
	else:
		print("No open ports found")

def main():
	target_host = "example.com"  # Replace with the target host IP or domain
	target_ports = [80, 443, 22, 21, 3389]  # List of target ports to scan
	
	print(f"Scanning {target_host}...")
	open_ports = port_scan(target_host, target_ports)
	print_open_ports(open_ports)
	print("Scan complete.")

if __name__ == "__main__":
	main()
