import socket
import threading

Machine = input("Enter the IP address or hostname of the machine to scan: ")
print(f"Scanning ports on machine: {Machine}")

Ports = ((80, 443, 8080, 22, 21),(135, 139, 445))#The ports to be scanned
#80 is the default HTTP
#443 is the default HTTPS
#8080 is the default HTTP alternative
#22 is the default SSH
#21 is the default FTP

#135 is the default RPC
#139 is the default NetBIOS
#445 is the default SMB

open_ports = []#This list will store the open ports found during the scan

def scan_ports(Ports):
    for port in Ports:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)#This creates a socket object which is used to connections TCP
        sock.settimeout(1)#This sets a timeout of 1 second for the connection attempt
        result = sock.connect_ex((Machine, port))#IF the connection is successful, it returns 0, otherwise it returns an error code
        if result == 0:
            print(f"The port {port} is open")
            open_ports.append(port)
        else:
            print(f"The port {port} is closed")
        sock.close()

thread = threading.Thread(target=scan_ports, args=(Ports[0],))
thread.start()
scan_ports(Ports[1])
thread.join()#This waits for the thread to finish before continuing
print(f"Open ports found in {Machine}:")
for port in open_ports:
    print(port)
