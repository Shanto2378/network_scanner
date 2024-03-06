#!/usr/bin/env python

import scapy.all as scapy  # in terminal run sudo su then in root terminal run scapy it will install scapy in root mode then the dependency error will be resolved
# running scapy in root mode is not recommended but it is the only way to resolve the dependency error it will not fix anything on normal user mode please be aware of that fact.

def scan(ip):
    arp_request = scapy.ARP(pdst = ip) # creating an ARP request object
    broadcast = scapy.Ether(dst = "ff:ff:ff:ff:ff:ff") # creating an Ether object
    arp_request_broadcast = broadcast/arp_request # combining the two objects
    print(arp_request_broadcast.summary()) # printing the summary of the object


scan("192.168.225.1/24") # calling the function with the ip address of the network

