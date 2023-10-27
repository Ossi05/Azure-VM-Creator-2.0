import configparser
import subprocess
from VMInfo import SetVMInfo
from CreateVM import CreateVM
from colorama import Fore, Style
import pyfiglet
import os
from time import sleep
from DeleteVM import DeleteVM

config = None

def main():   

    global config
    config = configparser.ConfigParser()
    config.read("config.ini")     
    PrintCLI()   

def print_title(title):
    ClearScreen()
    print("\n")
    title = pyfiglet.figlet_format(title, font="ansi_regular")

    print(Fore.LIGHTBLUE_EX + title + Style.RESET_ALL)

        
def ClearScreen():
    os.system('cls' if os.name == 'nt' else 'clear')


def print_menu():
    print_title("Azure VM Creator")
    print(Fore.CYAN + Style.BRIGHT + "Options" + Style.RESET_ALL)
    print(Fore.LIGHTYELLOW_EX + "  1. Create Windows VM")
    print(Fore.LIGHTYELLOW_EX + "  2. Create Linux VM")
    print(Fore.LIGHTGREEN_EX + "  3. Edit Settings" + Style.RESET_ALL)
    print(Fore.LIGHTRED_EX + "  4. Delete VM" + Style.RESET_ALL)   
    print(Fore.LIGHTRED_EX + "  5. Exit" + Style.RESET_ALL)

def PrintCLI(): 
    while True:   
        ClearScreen() 
        print_menu()         
        try: 
            vmType = int(input(Fore.LIGHTYELLOW_EX + "Choose option: " + Style.RESET_ALL))
            
            if vmType == 1:
                CreateWindowsVM()            
            elif vmType == 2:
                CreateLinuxVM()               
            elif vmType == 3:
                subprocess.call(['notepad.exe', 'config.ini'])
                ClearScreen()            
            elif vmType == 4:
                HandleVMDelete()                 
            elif vmType == 5:
                quit()
            else:
                raise ValueError
        except ValueError:
            print(Fore.LIGHTRED_EX + "  Please choose a valid option" + Style.RESET_ALL)
            sleep(1.5)             
            continue



def CreateWindowsVM():

    chosenSize = ""
    eightGB = config.get('Windows', '8GB')
    sixteenGB = config.get('Windows', '16GB')

    while True:
        ClearScreen()
        print_title("Azure VM Creator")
        try:            
            print(Fore.CYAN + Style.BRIGHT + "Windows VM:" + Style.RESET_ALL)  
            print(Fore.CYAN + Style.BRIGHT + "How much RAM? Default 8 GB" + Style.RESET_ALL)
            print(Fore.LIGHTYELLOW_EX + "  [1] 8 GB")   
            print(Fore.LIGHTYELLOW_EX + "  [2] 16 GB" + Style.RESET_ALL) 
            print(Fore.LIGHTRED_EX + "  [3] Go Back" + Style.RESET_ALL)
            size = int(input(Fore.LIGHTYELLOW_EX + "Choose option: " + Style.RESET_ALL))
            if size == "":
                chosenSize = eightGB
                break
            elif size == 1:
                chosenSize = eightGB
                break
            elif size == 2:
                chosenSize = sixteenGB    
                break      
            elif size == 3:
                ClearScreen()
                PrintCLI()
                break
            else:
                raise ValueError
        except ValueError:
            print(Fore.LIGHTRED_EX + "  Please choose a valid option or leave blank for default" + Style.RESET_ALL)
            sleep(1.5)
            continue
    
    SetVMInfo("Windows", chosenSize)
    ClearScreen()
    CreateVM()



def CreateLinuxVM():
    
    chosenSize = ""

    # Ram sizes
    halfGB = config.get('Linux', '05GB')
    oneGB =  config.get('Linux', '1GB')
    fourGB =  config.get('Linux', '4GB')   

    while True:
        ClearScreen()
        print_title("Azure VM Creator")
        try:
            print(Fore.CYAN + Style.BRIGHT + "Linux VM:" + Style.RESET_ALL)
            print(Fore.CYAN + Style.BRIGHT + "How much RAM? Default 0.5 GB" + Style.RESET_ALL)
            print(Fore.LIGHTYELLOW_EX + "  [1] 0.5 GB")
            print(Fore.LIGHTYELLOW_EX + "  [2] 1 GB")
            print(Fore.LIGHTYELLOW_EX + "  [3] 4 GB" + Style.RESET_ALL)
            print(Fore.LIGHTRED_EX + "  [4] Go Back" + Style.RESET_ALL)
            size = int(input(Fore.LIGHTYELLOW_EX + "Choose option: " + Style.RESET_ALL))
            if size == "":
                chosenSize = halfGB
                break
            elif size == 1:
                chosenSize = halfGB
                break
            elif size == 2:
                chosenSize = oneGB
                break
            elif size == 3:
                chosenSize = fourGB
                break
            elif size == 4:
                ClearScreen()
                PrintCLI()
                break
            else:
                raise ValueError
        except ValueError:
            print(Fore.LIGHTRED_EX + "  Please choose a valid option or leave blank for default" + Style.RESET_ALL)
            sleep(1.5)
            continue



    SetVMInfo("Linux" , chosenSize)
    ClearScreen()
    CreateVM()
    
def HandleVMDelete():
    while True:
        delete = input(Fore.LIGHTYELLOW_EX + "Are you sure you want to delete the vm? yes (Y) no (n) " + Style.RESET_ALL)

        try:
            if delete.lower() == "y" or delete == "":
                DeleteVM()
                
                break
            elif delete.lower() == "n":
                print(Fore.LIGHTGREEN_EX + "  Returning to main menu" + Style.RESET_ALL)
                sleep(1.5)
                ClearScreen()
                PrintCLI()
            else:
                raise ValueError
        except ValueError:
            print(Fore.LIGHTRED_EX + "  Please choose a valid option" + Style.RESET_ALL)
            sleep(1.5)
            continue

if __name__ == "__main__":
    main()