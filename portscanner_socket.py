"""
port scanner script using only socket
by @jaksptr
"""
import socket
import ipaddress
import re

ports_range_format = re.compile("([0-9]+)-([0-9]+)")
port_min = 0
port_max = 65535
print("===================")
print("====PORTSCANNER====")
print("=====@jaksptr======")
print("======socket=======")

while True:
    ip_add_input = input("Enter IP address to scan: ")
    try:
        ip_address = ipaddress.ip_address(ip_add_input)
        break
    except:
        try:
            ip_address = socket.gethostbyname(ip_add_input)
            break
        except:
            print("invalid ip address or domain name")

while True:
    ports_input = input("Input port range to scan [beginning_port]-[end_port]: ")
    ports_valid = ports_range_format.search(ports_input.replace(" ", ""))

    if ports_valid:
        port_min = int(ports_valid.group(1))
        port_max = int(ports_valid.group(2))
        if port_min == port_max:
            print(f"start scanning port {port_max}, please wait...")
        elif port_min > port_max:
            print("invalid range")
            continue
        else:
            print(f"start scanning from port {port_min} to port {port_max}")
            print("listing opened port(s), please wait...")
        break

for port in range(port_min, port_max + 1):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(1)
            s.connect((ip_add_input, port))
            s.close()
            print(f"IP {ip_address} port {port} is OPEN")
    except:
        # print(f"IP {ip_add_input} port {port} is closed")
        pass
