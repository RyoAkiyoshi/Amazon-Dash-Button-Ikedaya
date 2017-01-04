#!/usr/bin/env python
# -*- coding: utf-8 -*-

from scapy.all import *
import json

f = open('config.json', 'r')
jsonData = json.load(f)
macaddress = jsonData['device']['macaddress']

def arp_display(pkt):
    if pkt[ARP].op == 1:
        if pkt[ARP].hwsrc == macaddress:
            print("池田屋行きたい")

if __name__ == '__main__':
    sniff(prn=arp_display, filter="arp", store=0)
