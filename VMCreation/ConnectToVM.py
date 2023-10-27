from time import sleep
import os

# 7 - Connect to VM
def ConnectToVM(ip_address_result, vmData):
    
    if (vmData.VMtype == "Windows"):
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"Connect with this command: mstsc /v:{ip_address_result.ip_address}")
        os.system(f'cmd /k "mstsc /v:{ip_address_result.ip_address}"')

    else:
        print("Connecting to vm in 5 seconds")
        os.system('cls' if os.name == 'nt' else 'clear')
        sleep(5)
        print(f"ssh {vmData.username}@{ip_address_result.ip_address}")
        os.system(f'cmd /k "ssh {vmData.username}@{ip_address_result.ip_address}"')

    print("Closing in 10 seconds")
    sleep(10)