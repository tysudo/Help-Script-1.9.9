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
print('(1)Run Train')
print('(2)HTOP')
print('(3)List directory of choice')
print('(4)Open Google Chrome and search.')
print('(5)Open all my favorite apps')
print('(6)Open cool webpage')
print('(7)If you have not installed the install script press 7')
print('(8)Enter Windows CMD with wine')
print('(9)Not sus at all? ? ? ?')
print('(10)Clone some thing off Github')
print('(11)Watch funny video to make you happier')
print('(12)Cool music to listen ')
print('(13)Install a package')

#
#pick
pick = int(input(f"{Fore.GREEN + Style.BRIGHT}Pick what you want to do: "))
if pick==1:
    os.system('sl')
if pick==2:
    os.system('htop') 
if pick==3:
    var2 = input(f"{Fore.GREEN}Please enter path: ")
    os.system('ls '+var2+'')
if pick==4:
    var3 = input(f'{Fore.GREEN}Please enter what you want to search. Spaces must be dashes: ')
    os.system('google-chrome https://www.google.com/search?q='+var3+' ')
if pick==5:
    os.system('discord && google-chrome')
if pick==6:
    os.system('google-chrome https://www.lingscars.com/')
if pick==7:
    var4 = str(input(f'{Fore.GREEN}Are you are Mac or Linux. cAsE SenSiTiVe : '))
    if var4=="Mac":
        os.system('sh ./install_mac.sh')
    if var4=="Linux":
        os.system('sudo sh ./install_linux.sh')
    else:
        print(f'{Fore.RED}FATAL ERROR!!!')
if pick==8:
    os.system('wine cmd')
if pick==9:
    os.system('say oga boga. oga boga')
if pick==10:
    var5 = input ('What repo do you wan to clone: ')
    os.system('git clone '+var5+' cloned')
    print(f'{Fore.RED}You cloned it in a folder called cloned')
if pick==11:
    os.system('google-chrome https://www.youtube.com/watch?v=R-RZ1OrjtQw')
if pick==12:
    os.system('google-chrome https://www.youtube.com/watch?v=Et3G7JSw4fQ')
if pick==13:
    var6 = str(input(f'{Fore.GREEN}Are you on Mac or Linux. cAsE SenSiTiVe: '))
    if var6=="Mac":
        var7 = str(input('What package would you like to install: '))
        os.system('brew install '+var7+'')
    if var6=="Linux":
        var8 = str(input('What package would you like to install: '))
        os.system('sudo apt install '+var8+' -y')
        
    
#pick end

    
#  
#
#
# 
#
#
#
else:
    print(Fore.RED +Style.BRIGHT + "FATAL ERROR, you stoped the script")
    
    
    