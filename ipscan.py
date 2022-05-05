import socket
from IPy import IP

ipaddress = input(' [+] ENTER YOUR TARGET]:')


def scan_port(ipaddress, port):
    try:
        s = socket.socket()
        s.settimeout(0.5)
        s.connect((ipaddress, port))
        print('Port ' + str(port) + 'is open')
    except:
        print('Port '+ str(port) +' is closed')

for port in range(1, 100):
    scan_port(ipaddress, port)





