# 4 - Create the IP address
def CreateIPAddress(network_client, vmData):  

    poller = network_client.public_ip_addresses.begin_create_or_update(vmData.resource_group_name,
        vmData.ip_name,
        {
            "location": vmData.location,
            "sku": { "name": "Standard" },
            "public_ip_allocation_method": "Static",
            "public_ip_address_version" : "IPV4"
        }
    )

    ip_address_result = poller.result()

    print(f"Provisioned public IP address {ip_address_result.name} with address {ip_address_result.ip_address}")

    return ip_address_result