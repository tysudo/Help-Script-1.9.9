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

ChooseOS = str(input(f'{Fore.GREEN}What Operating System are you using, Linux or Mac or Quit? cAsE SeNsItIvE: '))
os.system('clear')
#eeeeeeeeeeeeeeeeeeeeeee
if ChooseOS == "Quit":
    exit()
#eeeeeeeeeeeeeeeeeeeeeee
if ChooseOS == "Tytan":
    print(f'{Fore.GREEN}Welcome back Tytan, how have you been?')
    os.system("say Welcome back Tytan, how have you been?")
    tytan = str(input('So.. Are you good of bad?: '))
    if tytan == "bad":
        os.system("say Ok, ok, ok let me get this straight ur mad right you have had a bad day.")
        os.system("chromium https://www.youtube.com/watch?v=DODLEX4zzLQ")
    if tytan == "good":
        print(f'{Fore.GREEN}(1)Open GitHub to add more to your script')
        print(f'{Fore.GREEN}(2)Open my awesome web browser')
        print(f'{Fore.GREEN}(3)open VSCODE')
        print(f'{Fore.GREEN}(4)Check the weather')
        tytan1 = str(input('What would you like to do: '))
        if tytan1 == 1:
            os.system('chromium https://github.com/tysudo/Help-Script')
        if tytan1 == 2:
            os.system('python3 browser.py')
            os.system('python3 Script.py')
        if tytan1 == 3:
            os.system('code')
        if tytan1 == 4:
            os.system('python3 weather.py')
            os.system('python3 Script.py')
            
#eeeeeeeeeeeeeeeeeeeeeee

if ChooseOS == "Linux":
    print("""  _    _      _                       _       _     __   ___   ____  
 | |  | |    | |                     (_)     | |   /_ | / _ \ |___ \ 
 | |__| | ___| |_ __    ___  ___ _ __ _ _ __ | |_   | || | | |  __) |
 |  __  |/ _ \ | '_ \  / __|/ __| '__| | '_ \| __|  | || | | | |__ < 
 | |  | |  __/ | |_) | \__ \ (__| |  | | |_) | |_   | || |_| | ___) |
 |_|  |_|\___|_| .__/  |___/\___|_|  |_| .__/ \__|  |_(_)___(_)____/ 
               | |                     | |                           
               |_|                     |_|                           """)
    print(f'{Fore.RED}Search')
    print(f'{Fore.RED}Wine')
    print(f'{Fore.RED}Install')
    print(f'{Fore.RED}Other')
    print(f'{Fore.RED}System')
    print(f'{Fore.RED}Quit')

    pick = str(input(f'{Fore.GREEN}What do you want to do: '))
  
    #eeeeeeeeeeeeeeeeeeeeeee
    if pick == "Quit":
        exit()
    #eeeeeeeeeeeeeeeeeeeeeee
 
    if pick == "Search":
        print("""   _____                     _     
  / ____|                   | |    
 | (___   ___  __ _ _ __ ___| |__  
  \___ \ / _ \/ _` | '__/ __| '_ \ 
  ____) |  __/ (_| | | | (__| | | |
 |_____/ \___|\__,_|_|  \___|_| |_|
                                   
                                   """)
        print(f'{Fore.GREEN}(1)Search Amazon.com')
        print(f'{Fore.GREEN}(2)Search DuckDuckGo')
        print(f'{Fore.GREEN}(3)Search YouTube')
        print(f'{Fore.GREEN}(4)Search NewEgg')
        print(f'{Fore.GREEN}(5)Search Google')
        print(f'{Fore.GREEN}(6)VSCODE Web Builder')
        print(f'{Fore.GREEN}(7)Quit')
        search = int(input(f'{Fore.GREEN}What do you want to do: '))
        if search == 1:
            var1 = str(input('What would you like to search for. Spaces must be +: '))
            os.system('chromium https://www.amazon.ca/s?k='+var1+'')
            os.system('python3 Script.py')
        if search == 2:
            var2 = str(input('What would you like to search for. Spaces must be +: '))
            os.system('chromium https://duckduckgo.com/?q='+var2+' ')
            os.system('python3 Script.py')
        if search == 3:
            var3 = str(input('What would you like to search for. Spaces must be +: '))
            os.system('chromium https://www.youtube.com/results?search_query='+var3+'')
            os.system('python3 Script.py')
        if search == 4:
            var4 = str(input('What would you like to search for. Spaces must be +: '))
            os.system('chromium https://www.newegg.ca/p/pl?d='+var4+'')
            os.system('python3 Script.py')
        if search == 5:
            var5 = str(input('What would you like to search for. Spaces must be +: '))
            os.system('chromium https://www.google.com/search?q='+var5+'')
            os.system('python3 Script.py')
        if search == 6:
            os.system('chromium vscode.dev')
            os.system('python3 Script.py')
        if search == 7:
            exit()
  
    #eeeeeeeeeeeeeeeeeee
 
    if pick == "Wine":
        print(""" __          ___            
 \ \        / (_)           
  \ \  /\  / / _ _ __   ___ 
   \ \/  \/ / | | '_ \ / _ \
    \  /\  /  | | | | |  __/
     \/  \/   |_|_| |_|\___|
                            
                            """)
        print(f'{Fore.GREEN}(1)Wine CMD')
        wine = int(input(f'{Fore.GREEN}What would you like to do: '))
        if wine == 1:
            os.system('wine cmd')
            os.system('python3 Script.py')
  
    #eeeeeeeeeeeeeeeeeeeeeeeeee
   
    if pick == "Install":
        os.system('sudo sh ./install_linux.sh')
        os.system('python3 Script.py')

    #eeeeeeeeeeeeeeeeeeeeeeeee
  
    if pick == "Other":
        print("""   ____  _   _               
  / __ \| | | |              
 | |  | | |_| |__   ___ _ __ 
 | |  | | __| '_ \ / _ \ '__|
 | |__| | |_| | | |  __/ |   
  \____/ \__|_| |_|\___|_|   
                             
                             """)
        print(f'{Fore.GREEN}(1)Not sus at all')
        print(f'{Fore.GREEN}(2)coolish webpage')
        print(f'{Fore.GREEN}(3)Cool music to listen to')
        print(f'{Fore.GREEN}(4)Funny video to make you happier')
        Other = int(input(f'{Fore.GREEN}What would you like to do: '))
        if Other == 1:
            os.system('say oga boga. oga boga')
            os.system('python3 Script.py')
        if Other == 2:
            os.system('chromium https://www.lingscars.com')
            os.system('python3 Script.py')
        if Other == 3:
            os.system('chromium https://www.youtube.com/watch?v=Et3G7JSw4fQ')
            os.system('python3 Script.py')
        if Other == 4:
            os.system('chromium https://www.youtube.com/watch?v=R-RZ1OrjtQw')
            os.system('python3 Script.py')

    #eeeeeeeeeeeeeeeeeeeeeeeeeee

    if pick == "System":
        print("""   _____           _                 
  / ____|         | |                
 | (___  _   _ ___| |_ ___ _ __ ___  
  \___ \| | | / __| __/ _ \ '_ ` _ \ 
  ____) | |_| \__ \ ||  __/ | | | | |
 |_____/ \__, |___/\__\___|_| |_| |_|
          __/ |                      
         |___/                       """)
        print(f'{Fore.GREEN}(1)Run train')
        print(f'{Fore.GREEN}(2)HTOP')
        print(f'{Fore.GREEN}(3)Search directory')
        print(f'{Fore.GREEN}(4)Clone somthing off of Github')
        print(f'{Fore.GREEN}(5)Make a File')
        print(f'{Fore.GREEN}(6)Open our custom web browser')
        print(f'{Fore.GREEN}(7)Check the weather')
        System = int(input('What would you like to do: '))
        if System == 1:
            os.system('sl')
            os.system('python3 Script.py')
        if System == 2:
            os.system('htop')
            os.system('python3 Script.py')
        if System == 3:
            var7 = str(input(f'{Fore.GREEN}What directory would you like to search: '))
            os.system('ls '+var7+'')
            os.system('python3 Script.py')
        if System == 4:
            var8 = str(input(f'{Fore.GREEN}What would you like to clone: '))
            os.system('git clone '+var8+' cloned')
            os.system('python3 Script.py')
        if System == 5:
            var9 = str(input(f'{Fore.GREEN}What file would you like to make. EX python.py: '))
            os.system('touch '+var9+'')
            os.system('python3 Script.py')
        if System == 6:
            os.system('python3 browser.py')
            os.system('python3 Script.py')
        if System == 7:
            os.system('python3 weather.py')
            os.system('python3 Script.py')



#eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee

# IF CHOOSE Mac

#eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee   



if ChooseOS =="Mac":
    print(f'{Fore.RED}Search')
    print(f'{Fore.RED}Wine')
    print(f'{Fore.RED}Install')
    print(f'{Fore.RED}Other')
    print(f'{Fore.RED}System')
    print(f'{Fore.RED}Quit')

    pick = str(input(f'{Fore.GREEN}What do you want to do: '))
    #eeeeeeeeeeeeeeeeeeeeeee
    if pick == "Quit":
        exit()
    #eeeeeeeeeeeeeeeeeeeeeee

    if pick == "Search":
        print(f'{Fore.GREEN}(1)Search Amazon.com')
        print(f'{Fore.GREEN}(2)Search DuckDuckGo')
        print(f'{Fore.GREEN}(3)Search YouTube')
        print(f'{Fore.GREEN}(4)Search NewEgg')
        print(f'{Fore.GREEN}(5)Search Google')
        print(f'{Fore.GREEN}(6)VSCODE Web Builder')
        print(f'{Fore.GREEN}(7)Quit')        
        search = int(input(f'{Fore.GREEN}What do you want to do: '))
        if search == 1:
            var1 = str(input('What would you like to search for. Spaces must be +: '))
            os.system('open -a "Google Chrome" https://www.amazon.ca/s?k='+var1+'')
            os.system('python3 Script.py')
        if search == 2:
            var2 = str(input('What would you like to search for. Spaces must be +: '))
            os.system('open -a "Google Chrome" https://duckduckgo.com/?q='+var2+' ')
            os.system('python3 Script.py')            
        if search == 3:
            var3 = str(input('What would you like to search for. Spaces must be +: '))
            os.system('open -a "Google Chrome" https://www.youtube.com/results?search_query='+var3+'')
            os.system('python3 Script.py')
        if search == 4:
            var4 = str(input('What would you like to search for. Spaces must be +: '))
            os.system('open -a "Google Chrome" https://www.newegg.ca/p/pl?d='+var4+'')
            os.system('python3 Script.py')
        if search == 5:
            var5 = str(input('What would you like to search for. Spaces must be +: '))
            os.system('open -a "Google Chrome" https://www.google.com/search?q='+var5+'')
            os.system('python3 Script.py')
        if search == 6:
            os.system('open -a "Google Chrome" https://vscode.dev')
            os.system('python3 Script.py')
        if search == 7:
            exit()            
 
    #eeeeeeeeeeeeeeeeeee
   
    if pick == "Wine":
        print(f'{Fore.GREEN}(1)Wine CMD')
        wine = int(input(f'{Fore.GREEN}What would you like to do: '))
        if wine == 1:
            os.system('wine cmd')
            os.system('python3 Script.py')
   
    #eeeeeeeeeeeeeeeeeeeeeeeeee
  
    if pick == "Install":
        os.system('sh ./install_mac.sh')
        os.system('python3 Script.py')

    #eeeeeeeeeeeeeeeeeeeeeeeee
   
    if pick == "Other":
        print(f'{Fore.GREEN}(1)Not sus at all')
        print(f'{Fore.GREEN}(2)coolish webpage')
        print(f'{Fore.GREEN}(3)Cool music to listen to')
        print(f'{Fore.GREEN}(4)Funny video to make you happier')
        Other = int(input(f'{Fore.GREEN}What would you like to do: '))
        if Other == 1:
            os.system('say oga boga. oga boga')
            os.system('python3 Script.py')
        if Other == 2:
            os.system('open -a "Google Chrome" https://www.lingscars.com')
            os.system('python3 Script.py')
        if Other == 3:
            os.system('open -a "Google Chrome" https://www.youtube.com/watch?v=Et3G7JSw4fQ')
            os.system('python3 Script.py')
        if Other == 4:
            os.system('open -a "Google Chrome" https://www.youtube.com/watch?v=R-RZ1OrjtQw')
            os.system('python3 Script.py')
   
    #eeeeeeeeeeeeeeeeeeeeeeeeeee
  
    if pick == "System":
        print(f'{Fore.GREEN}(1)Run train')
        print(f'{Fore.GREEN}(2)HTOP')
        print(f'{Fore.GREEN}(3)Search directory')
        print(f'{Fore.GREEN}(4)Clone somthing off of Github')
        print(f'{Fore.GREEN}(5)Make a file')
        System = int(input('What would you like to do: '))
        if System == 1:
            os.system('sl')
            os.system('python3 Script.py')
        if System == 2:
            os.system('htop')
            os.system('python3 Script.py')
        if System == 3:
            var7 = str(input(f'{Fore.GREEN}What directory would you like to search: '))
            os.system('ls '+var7+'')
            os.system('python3 Script.py')
        if System == 4:
            var8 = str(input(f'{Fore.GREEN}What would you like to clone: '))
            os.system('git clone '+var8+' cloned')
            os.system('python3 Script.py')
        if System == 5:
            var6 = str(input(f'{Fore.GREEN}What file would you like to make: '))
            os.system('touch '+var6+'')
            os.system('python3 Script.py')
else:
    print(f'{Fore.RED + Style.BRIGHT }Sorry for this error. Please report it to https://github.com/tysudo/Help-Script/issues')
    os.system('python3 Script.py')
 
    
        
    
        