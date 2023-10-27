import configparser
from time import sleep


VMData = None

class VMData:
    def __init__(self, azure_id, username, password, resource_group_name, location, vnet_name, subnet_name, ip_name, ip_config_name, nic_name, nsg_name, vm_name, publisher, offer, sku, version, RAMAmount, VMtype):
        self.azure_id = azure_id
        self.username = username
        self.password = password
        self.resource_group_name = resource_group_name
        self.location = location
        self.vnet_name = vnet_name
        self.subnet_name = subnet_name
        self.ip_name = ip_name
        self.ip_config_name = ip_config_name
        self.nic_name = nic_name
        self.nsg_name = nsg_name
        self.vm_name = vm_name
        self.publisher = publisher
        self.offer = offer
        self.sku = sku
        self.version = version
        self.RAMAmount = RAMAmount
        self.VMtype = VMtype
        
    

def SetVMInfo(VMtype, chosenSize):
    # Add config values to VMData object
    config = configparser.ConfigParser()
    config.read("config.ini")

    if (config.get('AzureSettings', 'azure_id') == ""):
        print("Please set your Azure id in config.ini")
        sleep(5)
        quit()


    global VMData

    VMData = VMData(
        config.get('AzureSettings', 'azure_id'),
        config.get('AzureSettings', 'username'),
        config.get('AzureSettings', 'password'),
        config.get('AzureSettings', 'resource_group_name'),
        config.get('AzureSettings', 'location'),
        config.get('NETWORK', 'vnet_name'),
        config.get('NETWORK', 'subnet_name'),
        config.get('NETWORK', 'ip_name'),
        config.get('NETWORK', 'ip_config_name'),
        config.get('NETWORK', 'nic_name'),
        config.get('Security Rule', 'nsg_name'),
        config.get(VMtype, 'vm_name'),
        config.get(VMtype, 'publisher'),
        config.get(VMtype, 'offer'),
        config.get(VMtype, 'sku'),
        config.get(VMtype, 'version'),
        chosenSize,
        VMtype
    )

def GetVMInfo():
    return VMData

    
