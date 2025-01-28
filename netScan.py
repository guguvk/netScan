#!/usr/bin/python3

# netScan v1.0, Author @guguvk (Axel González)

#RUN AS ROOT

from scapy.all import ARP, Ether, srp

red="192.168.154.1/24"

arp = ARP(pdst=red)
ether = Ether(dst="ff:ff:ff:ff:ff:ff")
pkt = ether/arp
response = srp(pkt, timeout=6)[0]
devices=[]

for env, reci in response:
    devices.append({"IP":reci.psrc, "Mac":reci.hwsrc})

print("\nDispositivos detectados en la red")
print("")

for device in devices:
    print(device["IP"], device["Mac"])

