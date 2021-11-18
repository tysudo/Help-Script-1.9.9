import os
import sys
import tkinter
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)
import argparse
#args
parser = argparse.ArgumentParser(description='This is a script that will make your day faster.')
args = parser.parse_args()
#args end
#
print('(1)Quarantine File')
print('(2)Run Train')
print('(3)Scan desktop for viruses')
print('(4)HTOP')
print('(5)List directory of choice')
print('(6)Open Google Chrome and search')
print('(7)Open all my favorite apps')
print('(8)Open cool webpage')
print('(9)If you have not installed the install script press 9')
print('(10)Enter Windows CMD')
print('(11)Not sus at all? ? ? ?')
print('(12)clone some thing off Github')
#
#
pick = int(input(f"{Fore.GREEN}Pick what you want to do: "))
if pick==1:
#os.system('ls')
    var1 = input(f"{Fore.GREEN}Please enter path: ")
    os.system('savscan '+var1+' --quarantine')
if pick==2:
    os.system('sl')
if pick==3:
    os.system('savscan /home/tytan/Desktop')
if pick==4:
    os.system('htop') 
if pick==5:
    var2 = input(f"{Fore.GREEN}Please enter path: ")
    os.system('ls '+var2+'')
if pick==6:
    var3 = input(f'{Fore.GREEN}Please enter what you want to search. Has to be a webpage. ex. youtube.com: ')
    os.system('google-chrome  '+var3+' ')
if pick==7:
    os.system('discord && google-chrome')
if pick==8:
    os.system('google-chrome https://www.lingscars.com/')
if pick==9:
    var4 = int(input(f'{Fore.GREEN}Are you are Mac or Linux. Press 1 on if on Mac. Press 2 if on linux: '))
    if var4==1:
        os.system('sh ./install_mac.sh')
    if var4==2:
        os.system('sudo sh ./install_linux.sh')
    else:
        print(f'{Fore.RED}FATAL ERROR!!!')
if pick==10:
    os.system('wine cmd')
if pick==11:
    os.system('say oga boga. oga boga ')
if pick==12:
    var5 = input ('What repo do you wan to clone: ')
    os.system('git clone '+var5+' cloned')
    print(f'{Fore.RED}You cloned it in a folder called cloned')
    
#  
#
#
# 
#
#
#
else:
    print(Fore.RED +Style.BRIGHT + "FATAL ERROR, you stoped the script")
    
    