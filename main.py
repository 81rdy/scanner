#/bin/python3

            # TODO add possiblity to make a list of ip addresses to scan.

import os
import socket
from colorama import Fore
print('Hey, hey calm down! Its a lazy scanner it needs some time to do some streaches and such to start working.\n\nGo make yourself cup of coffee or tea.\n')
local = input('do you want to scan local network for potentail targets?:\n[y/N]:')
sweep = """
#!/bin/bash

local_networks=$(ifconfig | grep -Eo 'inet (addr:)?([0-9]*\.){2}[0-9]*' | grep -Eo '([0-9]*\.){2}[0-9]*' | grep -v '127.0.0')
echo $local_networks
for network in ${local_networks[@]}; do
    for ip in `seq 1 254`; do 
        ping -c 1 $network.$ip | grep "64 bytes" | cut -d " " -f 4 &
    done
done

"""
if local == "y":
    os.system(sweep)

def choice(mode):
    match mode:
        case "1":
            fullscan(ip) #fullscan is scanning all possible ports starting at 1 and ending at 65535
        case "2":
            custom_range(ip)
        case "3":
            most_popular(ip)
        case "4":
            custom_list(ip)
        case _:
            print(Fore.RED+"WRONG INPUT!!!")


def fullscan(ip):
    print(Fore.GREEN+'->FULLSCAN!<-')    
    for port in range(2,65535):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = sock.connect_ex((ip,port))
        
        if result == 0:
            print (Fore.RED+f'!!!~Port {port} is open~!!!')
        #else: 
            #print (Fore.WHITE+f'Port {port} is closed')
        sock.close()


def custom_range(ip):   
        print(Fore.GREEN+'->CUSTOM RANGE!<-')
        start = input('input starting port number: ')
        finish = input('input ending port value: ')
        print('\n')   
        #Secure casting from string to int ValueError
        try:
            for port in range(int(start),int(finish)):
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                socket.setdefaulttimeout(1)
                result = sock.connect_ex((ip,port))
                if result == 0: 
                    print (Fore.RED+f'!!!~Port {port} is open~!!!')
                #else: 
                    #print (Fore.WHITE+f'Port {port1} is closed')
                sock.close()
        except ValueError:
            print(Fore.RED+"ENTER A PROPER VALUE >:(")

def most_popular(ip):
    print(Fore.GREEN+'->MOST POPULAR!<-')   
    with open('most_popular.txt','r') as file:
        for port in file:
            port1 = port.split(' ')[0]
            port1 = int(port1)
            #print(port1)
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket.setdefaulttimeout(1)
            result = sock.connect_ex((ip,port1))
            if result == 0:
                print (Fore.RED+f'!!!~Port {port1} is open~!!!')
            #else:
                #print (Fore.WHITE+f'Port {port1} is closed')
            sock.close()


def custom_list(ip):
    path = input('input name/path to the custom file: ')
    print(Fore.GREEN+'->CUSTOM LIST!<-')   
    with open(path,'r') as file:
        for port in file:
            port1 = port.split(' ')[0]
            port1 = int(port1)
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket.setdefaulttimeout(1)
            result = sock.connect_ex((ip,port1))
            if result == 0:
                print (Fore.RED+f'!!!~Port {port1} is open~!!!')
            #else:
                #print (Fore.WHITE+f'Port {port1} is closed')
            sock.close()


while True:
    ip = input(Fore.BLUE+'insert IP/domain name: ')
    mode = input(Fore.YELLOW+'pick scanner mode 1-4\n\t>1.fullscan\n\t>2.custom range\n\t>3.most popular\n\t>4.custom list\n======>')
    choice(mode)
    print(Fore.RED+f'DONE!\n\n')
    
