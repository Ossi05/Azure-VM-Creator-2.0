from azure.mgmt.network import NetworkManagementClient
from azure.mgmt.network.models import NetworkSecurityGroup, SecurityRule

# 2 - provision the virtual network
def CreateVirtualNetwork(credential, subscription_id, vmData):
    
    # Get the management object for the network
    network_client = NetworkManagementClient(credential, subscription_id)

    # Create the virtual network 
    poller = network_client.virtual_networks.begin_create_or_update(vmData.resource_group_name,
        vmData.vnet_name,
        {
            "location": vmData.location,
            "address_space": {
                "address_prefixes": ["10.0.0.0/16"]
            }
        }
    )
    vnet_result = poller.result()

    print(f"Provisioned virtual network {vnet_result.name} with address prefixes {vnet_result.address_space.address_prefixes}")

    # Security Rules 
    print("Creating security rules")
    nsg_params = NetworkSecurityGroup(id= vmData.nsg_name, location=vmData.location, tags={ "name" : "Python" })
    nsg = network_client.network_security_groups.begin_create_or_update(vmData.resource_group_name, vmData.nsg_name, parameters=nsg_params)

    network_client.security_rules.begin_create_or_update(vmData.resource_group_name, vmData.nsg_name,"my_Port_8080",SecurityRule(
            protocol='Tcp', 
            source_address_prefix='*', 
            destination_address_prefix='*', 
            access='Allow', 
            direction='Inbound', description='my_Port_8080 use rules',source_port_range='*', 
            #destination_port_range="1000,2000",
            destination_port_ranges=["22","80","3389"],     
            priority=100, name="my_Port_8080"))
    
    print("**complete**")

    return network_client