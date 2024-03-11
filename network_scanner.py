#!/usr/bin/env python

import scapy.all as scapy  # in terminal run sudo su then in root terminal run scapy it will install scapy in root mode then the dependency error will be resolved
# running scapy in root mode is not recommended but it is the only way to resolve the dependency error it will not fix anything on normal user mode please be aware of that fact.
import argparse # importing the optparse module to parse the command line arguments

def get_arguments():
    parser = argparse.ArgumentParser() # creating an OptionParser object
    parser.add_argument("-t", "--target", dest = "target", help = "target Ip / Ip Range") # adding an option to the object
    options = parser.parse_args() # parsing the command line arguments
    return options # returning the options

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
 
options = get_arguments() # getting the command line arguments
scan_result = scan(options.target) # scanning the target IP / IP range
print_result(scan_result) # printing the result