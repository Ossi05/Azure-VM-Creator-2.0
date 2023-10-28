from azure.identity import DefaultAzureCredential
from VMInfo import GetVMInfo
import os
import colorama

from VMCreation.CreateResourceGroup import CreateResourceGroup
from VMCreation.CreateVirtualNetwork import CreateVirtualNetwork
from VMCreation.CreateSubnet import CreateSubnet
from VMCreation.CreateIPAddress import CreateIPAddress
from VMCreation.CreateNetworkInterfaceClient import CreateNetworkInterfaceClient
from VMCreation.CreateVirtualMachine import CreateVirtualMachine
from VMCreation.ConnectToVM import ConnectToVM

def CreateVM():
    vmData = GetVMInfo()

    # Set color to Fore.LIGHTYELLOW_EX
    print(colorama.Fore.LIGHTYELLOW_EX)

    print(f"Creating {vmData.VMtype} virtual machine")

    # Acquire credential object using CLI-based authentication.
    credential = DefaultAzureCredential()

    # Retrieve subscription ID from environment variable.
    subscription_id = os.environ["AZURE_SUBSCRIPTION_ID"] = vmData.azure_id

    CreateResourceGroup(credential, subscription_id, vmData.resource_group_name, vmData.location)
    network_client = CreateVirtualNetwork(credential, subscription_id, vmData)
    subnet_result = CreateSubnet(network_client, vmData)
    ip_address_result = CreateIPAddress(network_client, vmData)
    nic_result = CreateNetworkInterfaceClient(network_client, vmData, subnet_result, ip_address_result)
    CreateVirtualMachine(credential, subscription_id, vmData, nic_result)
    ConnectToVM(ip_address_result, vmData)
    print(colorama.Fore.RESET)