class ARP_RARP:
    def __init__(self):
        self.arp = {
            "192.168.1.1": "AA:BB:CC:DD:01",
            "192.168.1.2": "AA:BB:CC:DD:02"
        }
        self.rarp = {v: k for k, v in self.arp.items()}

    def arp_request(self, ip):
        print("ARP Request for", ip)
        print("MAC:", self.arp.get(ip, "Not Found"))

    def rarp_request(self, mac):
        print("RARP Request for", mac)
        print("IP:", self.rarp.get(mac, "Not Found"))


# Run
obj = ARP_RARP()

obj.arp_request("192.168.1.1")
obj.arp_request("192.168.1.5")

obj.rarp_request("AA:BB:CC:DD:01")
obj.rarp_request("AA:BB:CC:DD:99")