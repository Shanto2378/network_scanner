#!/usr/bin/env python

import scapy.all as scapy  # in terminal run sudo su then in root terminal run scapy it will install scapy in root mode then the dependency error will be resolved
# running scapy in root mode is not recommended but it is the only way to resolve the dependency error it will not fix anything on normal user mode please be aware of that fact.

def scan(ip):
    arp_request = scapy.ARP(pdst = ip) # creating an ARP request object
    broadcast = scapy.Ether(dst = "ff:ff:ff:ff:ff:ff") # creating an Ether object
    arp_request_broadcast = broadcast/arp_request # combining the two objects
    answered_list = scapy.srp(arp_request_broadcast, timeout = 1, verbose = False)[0] # sending the request and storing the answered and unanswered requests

    client_list = [] # creating an empty list to store the IP and MAC addresses of the answered requests
    print("-----------------------------------------") # printing the header
    for element in answered_list:
        client_dict = {"ip": element[1].psrc, "mac": element[1].hwsrc} # creating a dictionary to store the IP and MAC addresses of the answered requests
        client_list.append(client_dict) # appending the dictionary to the list
    return client_list # returning the list

def print_result(results_list):
    print("IP \t\t\t MAC Address\n-----------------------------------------") # printing the header
    for client in results_list:
        print(client["ip"] + "\t\t" + client["mac"]) # printing the IP and MAC addresses of the answered requests
 
scan_result = scan("10.0.2.1/24") # calling the function with the ip address of the network which is "route -n" 
print_result(scan_result)