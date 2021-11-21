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

ChooseOS = str(input(f'{Fore.GREEN}What Operating System are you using, Linux or Mac?: '))
#eeeeeeeeeeeeeeeeeeeeeee
if ChooseOS == "Linux":

    print(f'{Fore.RED + Style.BRIGHT }THIS IS A BETA SCRIPT. RUN AT OWN RISK')
    print('Search')
    print('Wine')
    print('Install')
    print('Other')
    print('System')

    pick = str(input(f'{Fore.GREEN}What do you want to do: '))
    #eeeeeeeeeeeeeeeeeeeeeee
    if pick == "Search":
        print(f'{Fore.GREEN}(1)Search Amazon.com')
        print(f'{Fore.GREEN}(2)Search DuckDuckGo')
        print(f'{Fore.GREEN}(3)Search YouTube')
        print(f'{Fore.GREEN}(4)Search NewEgg')
        print(f'{Fore.GREEN}(5)Search Google')
        search = int(input(f'{Fore.GREEN}What do you want to do: '))
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
    #eeeeeeeeeeeeeeeeeee
    if pick == "Wine":
        print(f'{Fore.GREEN}(1)Wine CMD')
        wine = int(input(f'{Fore.GREEN}What would you like to do: '))
        if wine == 1:
            os.system('wine cmd')
    #eeeeeeeeeeeeeeeeeeeeeeeeee
    if pick == "Install":
        print('(1)Install script')
        var6 = str(input(f'{Fore.GREEN}Are you are Mac or Linux. cAsE SeNsItIvE : '))
        if var6=="Mac":
            os.system('sh ./install_mac.sh')
        if var6=="Linux":
            os.system('sudo sh ./install_linux.sh')
    #eeeeeeeeeeeeeeeeeeeeeeeee
    if pick == "Other":
        print(f'{Fore.GREEN}(1)Not sus at all')
        print(f'{Fore.GREEN}(2)coolish webpage')
        print(f'{Fore.GREEN}(3)Cool music to listen to')
        print(f'{Fore.GREEN}(4)Funny video to make you happier')
        Other = int(input(f'{Fore.GREEN}What would you like to do: '))
        if Other == 1:
            os.system('say oga boga. oga boga')
        if Other == 2:
            os.system('google-chrome https://www.lingscars.com')
        if Other == 3:
            os.system('google-chrome https://www.youtube.com/watch?v=Et3G7JSw4fQ')
        if Other == 4:
            os.system('google-chrome https://www.youtube.com/watch?v=R-RZ1OrjtQw')
    #eeeeeeeeeeeeeeeeeeeeeeeeeee
    if pick == "System":
        print(f'{Fore.GREEN}(1)Run train')
        print(f'{Fore.GREEN}(2)HTOP')
        print(f'{Fore.GREEN}(3)Search directory')
        print(f'{Fore.GREEN}(4)Clone somthing off of Github')
        System = int(input('what would you like to do: '))
        if System == 1:
            os.system('sl')
        if System == 2:
            os.system('htop')
        if System == 3:
            var7 = str(input(f'{Fore.GREEN}What directory would you like to search: '))
            os.system('ls '+var7+'')
        if System == 4:
            var8 = str(input(f'{Fore.GREEN}What would you like to clone: '))
            os.system('git clone '+var8+' cloned')
            
if ChooseOS =="Mac":
    print(f'{Fore.RED + Style.BRIGHT }THIS IS A BETA SCRIPT. RUN AT OWN RISK')
    print('Search')
    print('Wine')
    print('Install')
    print('Other')
    print('System')

    pick = str(input(f'{Fore.GREEN}What do you want to do: '))
    #eeeeeeeeeeeeeeeeeeeeeee
    if pick == "Search":
        print(f'{Fore.GREEN}(1)Search Amazon.com')
        print(f'{Fore.GREEN}(2)Search DuckDuckGo')
        print(f'{Fore.GREEN}(3)Search YouTube')
        print(f'{Fore.GREEN}(4)Search NewEgg')
        print(f'{Fore.GREEN}(5)Search Google')
        search = int(input(f'{Fore.GREEN}What do you want to do: '))
        if search == 1:
            var1 = str(input('What would you like to search for. Spaces must be +: '))
            os.system('open -a "Google Chrome" https://www.amazon.ca/s?k='+var1+'')
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
    #eeeeeeeeeeeeeeeeeee
    if pick == "Wine":
        print(f'{Fore.GREEN}(1)Wine CMD')
        wine = int(input(f'{Fore.GREEN}What would you like to do: '))
        if wine == 1:
            os.system('wine cmd')
    #eeeeeeeeeeeeeeeeeeeeeeeeee
    if pick == "Install":
        print('(1)Install script')
        var6 = str(input(f'{Fore.GREEN}Are you are Mac or Linux. cAsE SeNsItIvE : '))
        if var6=="Mac":
            os.system('sh ./install_mac.sh')
        if var6=="Linux":
            os.system('sudo sh ./install_linux.sh')
    #eeeeeeeeeeeeeeeeeeeeeeeee
    if pick == "Other":
        print(f'{Fore.GREEN}(1)Not sus at all')
        print(f'{Fore.GREEN}(2)coolish webpage')
        print(f'{Fore.GREEN}(3)Cool music to listen to')
        print(f'{Fore.GREEN}(4)Funny video to make you happier')
        Other = int(input(f'{Fore.GREEN}What would you like to do: '))
        if Other == 1:
            os.system('say oga boga. oga boga')
        if Other == 2:
            os.system('google-chrome https://www.lingscars.com')
        if Other == 3:
            os.system('google-chrome https://www.youtube.com/watch?v=Et3G7JSw4fQ')
        if Other == 4:
            os.system('google-chrome https://www.youtube.com/watch?v=R-RZ1OrjtQw')
    #eeeeeeeeeeeeeeeeeeeeeeeeeee
    if pick == "System":
        print(f'{Fore.GREEN}(1)Run train')
        print(f'{Fore.GREEN}(2)HTOP')
        print(f'{Fore.GREEN}(3)Search directory')
        print(f'{Fore.GREEN}(4)Clone somthing off of Github')
        System = int(input('what would you like to do: '))
        if System == 1:
            os.system('sl')
        if System == 2:
            os.system('htop')
        if System == 3:
            var7 = str(input(f'{Fore.GREEN}What directory would you like to search: '))
            os.system('ls '+var7+'')
        if System == 4:
            var8 = str(input(f'{Fore.GREEN}What would you like to clone: '))
            os.system('git clone '+var8+' cloned')
 
    
        
    
        