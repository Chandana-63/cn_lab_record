import socket

def dns_lookup():
    domain = input("Enter domain name: ")

    try:
        # Get local DNS server (approximate)
        hostname = socket.gethostname()
        local_ip = socket.gethostbyname(hostname)

        # Get domain IP
        domain_ip = socket.gethostbyname(domain)

        print("\n--- DNS Lookup Result ---")
        print("Server:", hostname)
        print("Address:", local_ip)
        print("\nName:", domain)
        print("Address:", domain_ip)

    except socket.gaierror:
        print("Error: Unable to resolve domain")

if __name__ == "__main__":
    dns_lookup()