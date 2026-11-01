import socket

Machine = socket.gethostbyname(socket.gethostname()) #This is the IP address of the machine on which the script is running
print(f"Scanning ports on machine: {Machine}")

Ports = (80, 443, 8080, 22, 21)#The ports to be scanned
#80 is the default HTTP
#443 is the default HTTPS
#8080 is the default HTTP alternative
#22 is the default SSH
#21 is the default FTP

for port in Ports:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)#This creates a socket object which is used to connections TCP
    sock.settimeout(1)#This sets a timeout of 1 second for the connection attempt
    result = sock.connect_ex((Machine, port))#IF the connection is successful, it returns 0, otherwise it returns an error code
    if result == 0:
        print(f"The port {port} is open")
    else:
        print(f"The port {port} is closed")
    sock.close()
