#did this comment work?

import os
import sys
import tkinter
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)
import argparse
import scrapy
#args
parser = argparse.ArgumentParser(description='This is a script that will make your day faster.')
args = parser.parse_args()
#added another comment


print('Search')
print('Wine')
print('Install')
print('Other')
print('System')
pick = str(input(f'{Fore.GREEN}What do you want to do: '))
if pick == "Search":
    print(f'{Fore.GREEN}(1)Search Amazon.com')
    print(f'{Fore.GREEN}(2)Search DuckDuckGo')
    print(f'{Fore.GREEN}(3)Search YouTube')
    print(f'{Fore.GREEN}(4)Search NewEgg')
    print(f'{Fore.GREEN}(5)Search Google')
    search = int(input('What do you want to do: '))
    if search == 1:
        var1 = str(input('What would you like to search for. Spaces must be +: '))
        os.system('google-chrome https://www.amazon.ca/s?k='+var1+'')
    if search == 2:
        var2 = str(input('What would you like to search for. Spaces must be +: '))
        os.system('google-chrome https://duckduckgo.com/?q='+var2+' ')
    if search == 3:
        var3 = str(input('What would you like to search for. Spaces must be +: '))
        os.system('google-chrome https://www.youtube.com/results?search_query='+var3+'')
    if search == 4:
        var4 = str(input('What would you like to search for. Spaces must be +: '))
        os.system('google-chrome https://www.newegg.ca/p/pl?d='+var4+'')
    if search == 5:
        var5 = str(input('What would you like to search for. Spaces must be +: '))
        os.system('google-chrome https://www.google.com/search?q='+var5+'')
if pick == "Wine":
    print('(1)Wine CMD')
    wine = int(input('What would you like to do: '))
    if wine == 1:
        os.system('wine cmd')
if pick == "Install":
    print('(1)Install script')
    var6 = str(input(f'{Fore.GREEN}Are you are Mac or Linux. cAsE SeNsItIvE : '))
    if var6=="Mac":
        os.system('sh ./install_mac.sh')
    if var6=="Linux":
        os.system('sudo sh ./install_linux.sh')
if pick == "Other":
    print('(1)Not sus at all')
    print('(2)coolish webpage')
    Other = int(input('what would you like to do: '))
    if Other == 1:
        os.system('say oga boga. oga boga')
    if Other == 2:
        os.system('google-chrome https://www.lingscars.com')
if pick == "System":
    System = int(input('what would you like to do: '))
    print('(1)Run train')
    print('(2)HTOP')
    print('(3)')
        
    
        