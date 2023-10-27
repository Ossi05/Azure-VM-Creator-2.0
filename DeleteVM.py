from azure.identity import DefaultAzureCredential
from azure.mgmt.resource import ResourceManagementClient
import configparser
import os
import time

def DeleteVM():

    # Load configuration from config.ini
    config = configparser.ConfigParser()
    config.read("config.ini")
    
    # Get Azure ID and subscription ID from the config file
    azure_id = config.get('AzureSettings', 'azure_id')
    resource_group_name = config.get('AzureSettings', 'resource_group_name')

    # Create Azure credentials and Resource Management Client
    credential = DefaultAzureCredential()
    client = ResourceManagementClient(credential, azure_id)

    try: 
       
        print("Trying to delete resource group")
        #Delete VM
        delete_async_operation = client.resource_groups.begin_delete(resource_group_name)
        delete_async_operation = client.resource_groups.begin_delete("NetworkWatcherRG")
        print("Deleting resource group. This operation might take a few minutes ")
        print("If this takes a long time, please check your resources")
        print("https://portal.azure.com/#view/HubsExtension/BrowseAll")
        delete_async_operation.wait()

        print("Deleted resource group" )
        input("Press Enter to continue...")
    except Exception as e:
        print(f"Error you don't have anything to delete: {e}")
        time.sleep(10)
        exit()
