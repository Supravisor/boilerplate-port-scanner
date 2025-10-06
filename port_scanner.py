import socket
from common_ports import ports_and_services

def get_open_ports(target, port_range, verbose = False):
    open_ports = []
    url = ''
    ip_address = ''

    try:
        ip_address = socket.gethostbyname(target)
    except:
        try:
            url = socket.gethostbyaddr(target)
        except:
            if not url:
                return 'Error: Invalid hostname'
            else:
                return 'Error: Invalid IP address'

    first_port = port_range[0]
    last_port = port_range[1]
    results = ''

    return(open_ports)
