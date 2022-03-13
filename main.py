#/bin/python3
#import os ???
import socket
import colorama
from colorama import Fore
ip = input('insert IP/domain name: ')
print('Hey, hey calm down! Its a lazy scanner he needs some time to do streaches and such to start working.\n\nGo make yourself cup of coffee or tea.\n')
def longscan(ip):    
    for port in range(6,1000):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = sock.connect_ex((ip,port))
        if result == 0: 
            print (Fore.RED+'!!!~Port '+str(port)+' is open~!!!')
        else: 
            print (Fore.WHITE+f'Port {port} is closed')
        sock.close()
longscan(ip)
