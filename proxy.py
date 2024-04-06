import requests
import socks
import socket

def get_proxies(protocol):
    if protocol.lower() == 'https':
        response = requests.get('https://api.proxyscrape.com/v3/free-proxy-list/get?request=displayproxies&proxy_format=protocolipport&format=text')
        socks.set_default_proxy(socks.SOCKS5, '127.0.0.1', 9050) 
        socket.socket = socks.socksocket
        response = requests.get('https://api.proxyscrape.com/v3/free-proxy-list/get?request=displayproxies&proxy_format=protocolipport&format=text')
    elif protocol.lower() == 'start':
        response = requests.get('https://api.proxyscrape.com/v3/free-proxy-list/get?request=displayproxies&proxy_format=protocolipport&format=text')
    else:
        print("Invalid")
        return []

    if response.status_code == 200:
        proxies = response.text.split('\n')
        return proxies
    else:
        print("Failed")
        return []

def save_proxies_to_file(proxies, filename):
    with open(filename, 'w') as f:
        for proxy in proxies:
            f.write(proxy + '\n')

def main():
    protocol = input("Please type start:")
    proxies = get_proxies(protocol)
    if proxies:
        filename = f"{protocol.lower()}_proxies.txt"
        save_proxies_to_file(proxies, filename)
        print(f"{len(proxies)} proxies retrieved and saved to {filename}.")
    else:
        print("No proxies retrieved.")

if __name__ == "__main__":
    main()
