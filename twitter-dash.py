#!/usr/bin/env python
# -*- coding: utf-8 -*-

from scapy.all import *
import json
import twitter

f = open('config.json', 'r')
jsonData = json.load(f)
macaddress = jsonData['device']['macaddress']
consumer_key = jsonData['twitter']['consumer_key']
consumer_secret = jsonData['twitter']['consumer_secret']
access_token_key = jsonData['twitter']['access_token_key']
access_token_secret = jsonData['twitter']['access_token_secret']

def arp_display(pkt):
    if pkt[ARP].op == 1:
        if pkt[ARP].hwsrc == macaddress:
            comment = '池田屋行きたい'
            tweet(comment)
            print 'tweeted.'

def tweet(comment):
    api = twitter.Api(consumer_key=consumer_key,
                      consumer_secret=consumer_secret,
                      access_token_key=access_token_key,
                      access_token_secret=access_token_secret)
    api.PostUpdate(comment)

if __name__ == '__main__':
    sniff(prn=arp_display, filter="arp", store=0)
