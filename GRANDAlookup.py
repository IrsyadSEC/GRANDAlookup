import socket

def get_ip_address(website):
    try:
        ip = socket.gethostbyname(website)
        return ip
    except socket.gaierror:
        return "Invalid domain or unreachable"

websites = [
    'example.com',
    'google.com',
    'facebook.com'
]

for website in websites:
    ip_address = get_ip_address(website)
    print(f'{website}: {ip_address}')
