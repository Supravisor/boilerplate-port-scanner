import socket
from common_ports import ports_and_services

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.settimeout(50)

def get_open_ports(target, port_range, verbose = False):
    open_ports = []
    url = ''
    ip_address = ''

    try:
        ip_address = socket.gethostbyname(target)
        url = target
    except:
        try:
            url = socket.gethostbyaddr(target)
            ip_address = target
        except:
            if not url:
                return 'Error: Invalid hostname'
            else:
                return 'Error: Invalid IP address'

    first_port = port_range[0]
    last_port = port_range[1]
    results = ''

    for port in range(first_port, last_port + 1):
        if not s.connect_ex((ip_address, port)):
            open_ports.append(port)

    if verbose == True:
        results = results + f'Open ports for {url} ({ip_address})'
        results = results + '\nPORT     SERVICE'
        for item in open_ports:
            results = results + f'\n{str(item):^3}      {ports_and_services[item]}'
        return str(results)
    else:
        return(open_ports)
