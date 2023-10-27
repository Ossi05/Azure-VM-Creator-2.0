# 3 - Create the subnet
def CreateSubnet(network_client, vmData):   

    print("Creating subnet")
    poller = network_client.subnets.begin_create_or_update(vmData.resource_group_name, 
        vmData.vnet_name, vmData.subnet_name,
        { "address_prefix": "10.0.0.0/24" }
    )
    subnet_result = poller.result()

    print(f"Provisioned virtual subnet {subnet_result.name} with address prefix {subnet_result.address_prefix}")

    return subnet_result