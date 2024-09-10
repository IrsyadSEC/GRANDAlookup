import socket
import pandas as pd

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

data = []

for website in websites:
    ip_address = get_ip_address(website)
    data.append({'Website': website, 'IP Address': ip_address})

df = pd.DataFrame(data)

df.to_excel('website_ip_addresses.xlsx', index=False)

print("IP addresses saved to website_ip_addresses.xlsx")
